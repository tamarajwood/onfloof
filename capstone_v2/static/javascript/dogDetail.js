const vm = new Vue ({
    el: '#dogDetail',
    delimiters: ['[[', ']]'],
    data: {
        pf: new petfinder.Client({apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7", secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw"}),
        dogData: {},
    },


    methods: {
        getDogData: function() {
            let dogId = window.location.pathname
            console.log(dogId)
            dogId = parseInt(dogId.substring(7, dogId.length))
            console.log(dogId)
            this.pf.animal.show(dogId).then(response => {
                this.dogData = response.data
            }).catch(err => {
                console.log(err.request, err.response);
                // See invalid parameters `err.invalidParams`
            })
        }
    },

    created: function() {
        this.getDogData()
    }
})