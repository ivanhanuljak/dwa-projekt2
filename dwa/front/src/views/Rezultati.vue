<template>
    <div id="rez">
        <div class="header">
            <h1>UNOS REZULTATA</h1>
            <H4>Unesite novu utakmicu</H4>
        </div>
        <div class="domacin">
            <b-form id="form-1">
                <b-form-group id="form-group-1" label="Odaberite domaci tim">
                    <b-form-select class="row-item odabirTima" v-model="timDomaci" @change="rendervModel(0)">
                        <option :value="null" disabled>Odaberite domacina</option>
                        <option v-for="tim in timovi" v-bind:value="[tim.id, tim.naziv, tim.igraci]" :key="tim.id"> {{ tim.naziv }}</option>
                    </b-form-select>
                </b-form-group>
            </b-form>
            <div>
                <ol class="lista-1">
                    <li v-for="d in timDomaci[2]" :key="d.id" >
                        <h4 style="text-align: left">{{d.ImeiPrezime}}</h4>
                    </li>
                </ol>
                <ul class="lista-2">
                    <li v-for="(v, index) in domacin.vModelList" :key="index">
                        <b-form-input class="inputi" @change="trenutnaUtakmica($event, 0)" type="number" v-model="v.bodovi" placeholder="Bodovi"></b-form-input>
                    </li>
                </ul>
            </div>
        </div>
        <div class="srednjiDiv">
            <h1>{{domacin.trenutnaUtakmica}} : {{gosti.trenutnaUtakmica}}</h1>
            <b-button-group style="margin-top:10%;">
                <b-button @click="racunanjeBodova()" variant="info">Spremi rezultat</b-button>
                <b-button @click="resetForm()" variant="danger" >Resetiraj</b-button>
                <b-button @click="azurirajPodatke()" variant="warning" >Azuriraj</b-button>
            </b-button-group>

        </div>
        <div class="gosti">
            <b-form id="form-2">
                <b-form-group id="form-group-2" label="Odaberite gostujuci tim">
                    <b-form-select class="row-item odabirTima" v-model="timGosti" @change="rendervModel(1)">
                        <option :value="null" disabled>Odaberite gosta</option>
                        <option v-for="tim in timovi" v-bind:value="[tim.id, tim.naziv, tim.igraci]" :key="tim.id"> {{ tim.naziv }}</option>
                    </b-form-select>
                </b-form-group>
            </b-form>

            <div>
                <ol class="lista-1">
                    <li v-for="d in timGosti[2]" :key="d.id" >
                        <h4 style="text-align: left">{{d.ImeiPrezime}}</h4>
                    </li>
                </ol>
                <ul class="lista-2">
                    <li v-for="(v, index) in gosti.vModelList" :key="index">
                        <b-form-input @change="trenutnaUtakmica($event, 1)" type="number" v-model="v.bodovi" placeholder="Bodovi"></b-form-input>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Rezultati",
        data () {
            return {
                timovi: [],
                bodoviIgraca: [],
                timDomaci: [],
                timGosti: [],
                domacin: {
                    idRez: '',
                    trenutnaUtakmica: 0,
                    vModelList: [],
                    ukupniBodovi: 0,
                    odigraneUtakmice: 0,
                    pobjedene: 0,
                    izgubljene: 0,
                    nerjeseno: 0,
                    bodNaLjestvici: 0,
                },
                gosti: {
                    idRez: '',
                    trenutnaUtakmica: 0,
                    vModelList: [],
                    ukupniBodovi: 0,
                    odigraneUtakmice: 0,
                    pobjedene: 0,
                    izgubljene: 0,
                    nerjeseno: 0,
                    bodNaLjestvici: 0,
                },
                odabraniTimoviIgraci: [],
                odabraniTimoviIgraciBodovi: [],
                rezultatiTimova: []
            }
        },
        created() {
            this.getTeam();
            this.getBodoviIgraca();
            this.getRezultati();
        },
        methods: {
            async getTeam () {
                await axios.get("http://127.0.0.1:5000/timovi")
                    .then((response) => {
                        this.timovi = response.data.timovi;
                    })
                    .catch((error) => {
                        alert('Ne mogu dohvatiti tim/ove. Greska: ', error);
                    });
            },
            async getBodoviIgraca () {
                await axios.get("http://127.0.0.1:5000/bodovi_igraca")
                    .then((response) => {
                        response.data.bodovi_igraca.forEach(function(value) {
                            this.bodoviIgraca.push(value);
                        }, this);
                    })
                    .catch((error) => {
                        alert('Ne mogu dohvatiti bodove igraca. Greka: ', error);
                    });
            },
            async getRezultati () {
                await axios.get("http://127.0.0.1:5000/rezultati_timova")
                    .then((response) => {
                        response.data.rezultati_timova.forEach(function(value) {
                            this.rezultatiTimova.push(value);
                        }, this);
                    })
                    .catch((error) => {
                        alert('Ne mogu dohvatiti rezultate. Greska: ', error);
                    });
            },
            rendervModel: function (index) {
                if(index){
                    this.gosti.vModelList = [];
                    this.timGosti[2].forEach(function() {
                        this.gosti.vModelList.push({bodovi: '' });
                    }, this);

                    this.rezultatiTimova.forEach(function (value) {
                        if (this.timGosti[0] === value.tim) {
                            this.gosti.idRez = value.id;
                            this.gosti.ukupniBodovi = value.bodovi;
                            this.gosti.odigraneUtakmice = value.utakmice;
                            this.gosti.pobjedene = value.pobjede;
                            this.gosti.izgubljene = value.izgubljene;
                            this.gosti.nerjeseno = value.nerjeseno;
                            this.gosti.bodNaLjestvici = value.ukupno;
                        }
                    }, this)
                }else{
                    this.domacin.vModelList = [];
                    this.timDomaci[2].forEach(function() {
                        this.domacin.vModelList.push({bodovi: '' });
                    }, this);

                    this.rezultatiTimova.forEach(function(value) {
                        if (this.timDomaci[0] === value.tim) {
                            this.domacin.idRez = value.id;
                            this.domacin.ukupniBodovi = value.bodovi;
                            this.domacin.odigraneUtakmice = value.utakmice;
                            this.domacin.pobjedene = value.pobjede;
                            this.domacin.izgubljene = value.izgubljene;
                            this.domacin.nerjeseno = value.nerjeseno;
                            this.domacin.bodNaLjestvici = value.ukupno;
                        }
                    }, this);
                }

            },
            trenutnaUtakmica : function (bod, index) {
                var pomocni = 0;
                if (index === 0) {
                    this.domacin.vModelList.forEach(function(value) {
                        pomocni = Number(pomocni) + Number(value.bodovi);
                    });
                    this.domacin.trenutnaUtakmica = pomocni;

                } else {
                    this.gosti.vModelList.forEach(function(value) {
                        pomocni = Number(pomocni) + Number(value.bodovi);
                    });
                    this.gosti.trenutnaUtakmica = pomocni;
                }
            },
            racunanjeBodova: function () {

                if(this.timDomaci[0] === this.timGosti[0]) {
                    alert('Oba tima su ista. Provjerite i unesite rezultate ponovno.');
                    return 0;
                }

                this.gosti.ukupniBodovi = Number(this.gosti.ukupniBodovi) + Number(this.gosti.trenutnaUtakmica);
                this.domacin.ukupniBodovi = Number(this.domacin.ukupniBodovi) + Number(this.domacin.trenutnaUtakmica);

                this.gosti.odigraneUtakmice = this.utakmice(this.gosti.odigraneUtakmice);
                this.domacin.odigraneUtakmice = this.utakmice(this.domacin.odigraneUtakmice);

                if (this.gosti.trenutnaUtakmica === this.domacin.trenutnaUtakmica) {
                    this.gosti.nerjeseno = this.nerjeseno(this.gosti.nerjeseno);
                    this.domacin.nerjeseno = this.nerjeseno(this.domacin.nerjeseno);
                }
                else if (this.gosti.trenutnaUtakmica > this.domacin.trenutnaUtakmica) {
                    this.gosti.pobjedene = this.pobjede(this.gosti.pobjedene);
                    this.gosti.bodNaLjestvici = Number(this.gosti.bodNaLjestvici) + 2;
                    this.domacin.izgubljene = this.izgubljeno(this.domacin.izgubljene);
                } else {
                    this.domacin.pobjedene = this.pobjede(this.domacin.pobjedene);
                    this.domacin.bodNaLjestvici = Number(this.domacin.bodNaLjestvici) + 2;
                    this.gosti.izgubljene = this.izgubljeno(this.gosti.izgubljene);
                }
                this.spremiRezultat();
                this.spremibodoveIgraca();
                this.resetForm();
            },
            utakmice : function (br) {
                return br = Number(br) + 1;
            },
            pobjede : function (br) {
                return br = Number(br) + 1;
            },
            izgubljeno : function (br) {
                return br = Number(br) + 1;
            },
            nerjeseno : function (br) {
                this.gosti.bodNaLjestvici = Number(this.gosti.bodNaLjestvici) + 1;
                this.domacin.bodNaLjestvici = Number(this.domacin.bodNaLjestvici) + 1;
                return br = Number(br) + 1;
            },
            spremiRezultat : function () {
                const rezultatDomaci = {
                  utakmice: this.domacin.odigraneUtakmice,
                  ukupno: this.domacin.bodNaLjestvici,
                  pobjede: this.domacin.pobjedene,
                  izgubljene: this.domacin.izgubljene,
                  nerjeseno: this.domacin.nerjeseno,
                  bodovi: this.domacin.ukupniBodovi,
                  tim: this.timDomaci[0]
                };
                const rezultatGosti = {
                    utakmice: this.gosti.odigraneUtakmice,
                    ukupno: this.gosti.bodNaLjestvici,
                    pobjede: this.gosti.pobjedene,
                    izgubljene: this.gosti.izgubljene,
                    nerjeseno: this.gosti.nerjeseno,
                    bodovi: this.gosti.ukupniBodovi,
                    tim: this.timGosti[0]
                };
                var duzinaListe = this.rezultatiTimova.length;
                if (duzinaListe === 0){
                    this.spremiNoviRezultat(rezultatDomaci);
                    this.spremiNoviRezultat(rezultatGosti);
                } else {
                    this.rezultatiTimova.forEach(function(value) {
                        if (value.tim === rezultatDomaci.tim) {
                            const rezDomaci = {
                                id: this.domacin.idRez,
                                utakmice: this.domacin.odigraneUtakmice,
                                ukupno: this.domacin.bodNaLjestvici,
                                pobjede: this.domacin.pobjedene,
                                izgubljene: this.domacin.izgubljene,
                                nerjeseno: this.domacin.nerjeseno,
                                bodovi: this.domacin.ukupniBodovi,
                                tim: this.timDomaci[0]
                            };
                            this.azurirajRezultat(rezDomaci);
                            return false;
                        }
                        duzinaListe = Number(duzinaListe) -1;
                        if (duzinaListe === 0) {
                            this.spremiNoviRezultat(rezultatDomaci);
                        }
                    }, this);
                    duzinaListe = this.rezultatiTimova.length;
                    this.rezultatiTimova.forEach(function(value) {
                        if (value.tim === rezultatGosti.tim) {
                            const rezGosti = {
                                id: this.gosti.idRez,
                                utakmice: this.gosti.odigraneUtakmice,
                                ukupno: this.gosti.bodNaLjestvici,
                                pobjede: this.gosti.pobjedene,
                                izgubljene: this.gosti.izgubljene,
                                nerjeseno: this.gosti.nerjeseno,
                                bodovi: this.gosti.ukupniBodovi,
                                tim: this.timGosti[0]
                            };
                            this.azurirajRezultat(rezGosti);
                            return false;
                        }
                        duzinaListe = Number(duzinaListe) -1;
                        if (duzinaListe === 0) {
                            this.spremiNoviRezultat(rezultatGosti);
                        }
                    }, this);
                }
            },
            azurirajRezultat : function (tim) {
                axios.put("http://127.0.0.1:5000/rezultati_timova", tim)
                    .then(() => {})
                    .catch(() => {
                    });
            },
            spremiNoviRezultat : function (tim) {
                axios.post("http://127.0.0.1:5000/rezultati_timova", tim)
                    .then(() => {})
                    .catch(() => {
                    });
            },
            spremibodoveIgraca : function () {
                var novo = [];
                var azuriranje = [];
                var duzinaListe = null;

                this.timDomaci[2].forEach(function(value, key) {
                    this.odabraniTimoviIgraci.push(value);
                    this.odabraniTimoviIgraciBodovi.push(this.domacin.vModelList[key].bodovi);
                }, this);
                this.timGosti[2].forEach(function(value, key) {
                    this.odabraniTimoviIgraci.push(value);
                    this.odabraniTimoviIgraciBodovi.push(this.gosti.vModelList[key].bodovi);
                }, this);
                this.odabraniTimoviIgraci.forEach(function(valueTim, key) {
                    duzinaListe = this.bodoviIgraca.length;
                    var trenutni = this.odabraniTimoviIgraciBodovi[key];
                    if (this.bodoviIgraca.length === 0) {
                        novo.push({bodovi: trenutni, igraci: valueTim.id});
                    } else {
                        this.bodoviIgraca.every(function(value) {
                            if (value.igraci === valueTim.id) {
                                trenutni = Number(trenutni) + Number(value.bodovi);
                                azuriranje.push({id: value.id, bodovi: trenutni, igraci: valueTim.id});
                                duzinaListe = Number(duzinaListe) - 1;
                                return false;
                            }
                            else if (duzinaListe > 0) {
                                duzinaListe = Number(duzinaListe) - 1;
                                if(duzinaListe === 0){
                                    novo.push({bodovi: trenutni, igraci: valueTim.id});
                                }
                                return true;
                            }
                        }, this);
                    }
                }, this);
                this.odabraniTimoviIgraci = [];
                this.odabraniTimoviIgraciBodovi = [];

                if(this.bodoviIgraca.length === 0) {
                    this.spremiBodoveIgracaNovi(novo);
                } else {
                    if (novo.length === 0) {
                        this.spremiBodoveIgracaAzuriranje(azuriranje);
                    }
                    else if (azuriranje.length === 0) {
                        this.spremiBodoveIgracaNovi(novo)
                    } else {
                        this.spremiBodoveIgracaAzuriranje(azuriranje);
                        this.spremiBodoveIgracaNovi(novo)
                    }
                }
            },
            async spremiBodoveIgracaNovi (bodNovi) {
                await axios.post("http://127.0.0.1:5000/bodovi_igraca", bodNovi)
                    .then(() => {
                    })
                    .catch(() => {
                    })
            },
            async spremiBodoveIgracaAzuriranje (bodAzuriranje) {
                await axios.put("http://127.0.0.1:5000/bodovi_igraca", bodAzuriranje)
                    .then(() => {
                    })
                    .catch(() => {
                    })
            },
            resetForm : function () {
                this.bodoviIgraca = [];
                this.timDomaci = {};
                this.timGosti = {};
                this.domacin.idRez = '';
                this.domacin.vModelList = [];
                this.domacin.trenutnaUtakmica = 0;
                this.gosti.idRez = '';
                this.gosti.vModelList = [];
                this.gosti.trenutnaUtakmica = 0;
                this.rezultatiTimova = [];
            },
            async azurirajPodatke () {
                this.resetForm();
                await this.getBodoviIgraca();
                await this.getRezultati();
            }
        }
    }
</script>

<style scoped>
    .domacin, .gosti{
        width: 25%;
        display: inline-block;
        background-color: aliceblue;
        border-radius: 10px;
        padding: 2.5%;
    }
    .domacin{
    }
    .srednjiDiv{
        display: inline-block;
        margin: 5% 10%;
    }
    .lista-1, .lista-2{
        display: inline-block;
    }
    .lista-1{
        float: left;
        margin-top: 1% !important;
        margin-left: -7%;
    }
    .lista-1 li{
        margin-top: 1.5% !important;
    }
    .lista-2{
        width: 40%;
        list-style-type: none;
    }

</style>