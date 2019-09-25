<template>
    <div id="Igrac">
        <div class="img">
            <b-img left alt="Naslovan slika" :src="image"></b-img>
        </div>
        <div class="forma">
            <b-form>
                <b-form-group id="input-group-1">
                    <b-form-input
                            id="input-1"
                            v-model="igrac.ImeiPrezime"
                            type="text"
                            required
                            placeholder="Upisite ime i prezime igraca"
                    ></b-form-input>

                    <b-form-input
                            id="input-2"
                            v-model="igrac.Datumrodenja"
                            type="text"
                            required
                            placeholder="Upišite datum rođenja igrača"
                    ></b-form-input>
                    <b-form-input
                            id="input-3"
                            v-model="igrac.Mjestorodenja"
                            type="text"
                            required
                            placeholder="Upišite mjesto rođenja igrača"
                    ></b-form-input>
                    <b-form-group label="Odaberite 'Dodaj sliku' prije spremanja igraca kako bi se slika spremila.">
                        <b-form-file
                                id="input-4"
                                v-model="igrac.slika"
                        ></b-form-file>
                    </b-form-group>
                </b-form-group>
            </b-form>
        </div>
            <b-button variant="success" v-on:click="konvertirajSliku" style="margin-right: 2%;">Dodaj sliku</b-button>
            <b-button variant="danger" v-on:click="onSubmit">Spremi igraca</b-button>
        <div>




        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "igrac",
        beforeMount(){
            this.getData();
        },
        mounted(){
            this.getData();
        },
        data () {
            return {
                igraci: null,
                igrac: {
                    ImeiPrezime: '',
                    Datumrodenja:'',
                    Mjestorodenja:'',
                    slika: null
                }
            }
        },

        methods: {
            getData() {

                axios.get("http://127.0.0.1:5000/igraci").then(({data}) => {
                    this.igraci = data.igraci;
                });
            },

            onSubmit : function () {
                const Igrac = {
                    ImeiPrezime: this.igrac.ImeiPrezime,
                    DatumRodenja:this.igrac.Datumrodenja,
                    MjestoRodenja: this.igrac.Mjestorodenja,
                    Slika: this.igrac.slika
                                                     };
                axios.post("http://127.0.0.1:5000/igraci", Igrac)
                    .then(() => {
                        this.igrac.Mjestorodenja= "";
                        this.igrac.Datumrodenja="";
                        this.igrac.ImeiPrezime= "";
                        this.igrac.slika= "";

                        alert("Igrac uspjesno spremljen");
                        this.getData();
                    })
                    .catch((error) => {
                        alert(error);
                    })
            },
            konvertirajSliku : function () {
                var self = this;
                var reader = new FileReader();
                var slika = new Blob([this.igrac.slika]);
                reader.readAsDataURL(slika);
                reader.onload = function () {
                    slika = reader.result;
                    self.igrac.slika = slika;
                };
            }
        },
        computed: {
            image () {
               return require('../assets/igrac.jpg');
            }
        }

    }
</script>

<style scoped>
    #input-group-1{
        width: 50%;
    }
    #input-1, #input-2, #input-3, #input-4{
        margin-bottom: 1%;
    }

</style>