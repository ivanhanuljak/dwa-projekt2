<template>
    <div id="liga">
        <h1>{{liga}}</h1>
        <div class="tablicaPozadina">
            <b-table id="tablicaLige" hover head-variant="dark" :items="prikazTablice" :fields="polja" caption-top>
                <template slot="table-caption">Odabirom bilo koje ekipe mozete vidjeti popis igraca i adresar te ekipe</template>
                <template slot="[metode]" slot-scope="row">
                    <b-button size="sm" variant="info" @click="otvoriDetalje(row)">Detalji</b-button>
                </template>
            </b-table>
        </div>

        <b-modal id="modal-lg" size="lg" v-model="detalji" hide-footer>
            <template slot="modal-header"><h2>{{trenutniRedak.ekipa}}</h2></template>
            <div>
                <ul class="lista">
                    <li v-for="igrac in trenutniRedak.igraci" :key="igrac.id">
                        <b-img rounded v-bind="opcije" :src="igrac.Slika" alt="Slika profila"></b-img>
                        <p style="display: inline-block; margin-left: 8%"><b>Ime i prezime: </b>{{igrac.ImeiPrezime}}<br>
                            <b>Datum rodenja: </b>{{igrac.DatumRodenja}}<br>
                            <b>Mjesto rodenja: </b>{{igrac.MjestoRodenja}}<br>
                            <b>Bodovi: </b>{{igrac.bodovi}}</p>
                    </li>
                </ul>
            </div>
        </b-modal>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Liga",
        data () {
            return {
                liga: '1. Hrvatska kuglacka liga - muski',
                polja: [
                    {key: 'ekipa', lable: 'Ekipa', sortable: true},
                    {key: 'uta', lable: 'UTA', sortable: true},
                    {key: 'pob', lable: 'POB', sortable: true},
                    {key: 'ner', lable: 'NER', sortable: true},
                    {key: 'por', lable: 'POR', sortable: true},
                    {key: 'bod', lable: 'BOD', sortable: true},
                    {key: 'poe', lable: 'POE', sortable: true},
                    {key: 'metode', label: 'Metoda'}
                ],
                timovi: [],
                rezultati: [],
                prikazTablice: [],
                detalji: false,
                trenutniRedak: {
                    ekipa: '',
                    igraci: []
                },
                opcije: { width: 135, height: 135}
            }
        },
        watch: {
          detalji(){
              if (this.detalji === false) {
                  this.trenutniRedak = [];
              }
          }
        },
        async created() {
            await this.getTeam();
            await this.getResoults();
            await this.getBodoviIgraca();
            this.punjenjeTablice();
        },
        methods: {
            async getTeam () {
                await axios.get("http://127.0.0.1:5000/timovi").then((data) => {
                    this.timovi = data.data.timovi;
                })
                    .catch(() => {
                        alert('Nisam u mogucnosti dohvatiti rezultate. Provjerite povezanost.');
                    })
            },
            async getResoults () {
                await axios.get("http://127.0.0.1:5000/rezultati_timova").then((data) => {
                    this.rezultati = data.data.rezultati_timova;
                })
                    .catch(() => {
                        alert('Nisam u mogucnosti dohvatiti rezultate. Provjerite povezanost.');
                    })
            },
            async getBodoviIgraca () {
              await axios.get("http://127.0.0.1:5000/bodovi_igraca")
                  .then((data) => {

                      var rez = data.data.bodovi_igraca;
                      this.spremanjeBodovauListu(rez);
                  })
                  .catch(() => {
                      alert('Nisam u mogucnosti dohvatiti bodove igraca. Provjerite povezanost.');
                  })
            },
            punjenjeTablice : function () {
                this.rezultati.forEach(function(value) {
                    var timId = value.tim;
                    this.timovi.every(function(valueT, keyT) {
                        if (timId === valueT.id) {
                            this.prikazTablice.push({inkex: keyT ,ekipa: valueT.naziv, uta: value.utakmice, pob: value.pobjede, ner: value.nerjeseno, por: value.izgubljene, bod: value.ukupno, poe: value.bodovi});
                            return false;
                        } else {
                            return true;
                        }
                    }, this)
                }, this);
            },
            otvoriDetalje : function (redak) {
                this.trenutniRedak.ekipa = '';
                this.trenutniRedak.igraci = [];
                this.trenutniRedak.ekipa = redak.item.ekipa;
                this.timovi.forEach(function(value) {
                    if (value.naziv === this.trenutniRedak.ekipa) {
                        value.igraci.forEach(function(igrac) {
                            this.trenutniRedak.igraci.push(igrac);
                        }, this);
                    }
                }, this);
                this.detalji = true;
            },
            spremanjeBodovauListu : function (r) {
                this.timovi.forEach(function(value) {
                    value.igraci.forEach(function(valueI) {
                        r.forEach(function(valueR) {
                            if (valueI.id === valueR.igraci) {
                                valueI.bodovi = valueR.bodovi;
                            }
                        });
                    });
                });
            }
        },
        computed: {
        }
    }
</script>

<style scoped>
    #tablicaLige{
        width: 100%;
        margin: 0;
    }
    .tablicaPozadina{
        background-color: aliceblue;
        margin: 4% 8%;
        border-radius: 10px;
        padding: 1% 4% 4% 4%;
    }
    .lista{
        position: relative;
        list-style-type: none;
    }
    .lista li p{
        position: absolute;
        margin-top: 3%;
    }
    .lista li{
        min-height: 140px;
        padding: 2%;
        position: relative;
        border-bottom: 1px solid gray;
        border-top: 1px solid gray;
    }

</style>