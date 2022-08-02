const dogFinder = new Vue ({
    el: '#adopt',
    delimiters: ['[[', ']]'],
    data: {
        pf: new petfinder.Client({apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7", secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw"}),

        activity: '',
        // activity will be selected by user via a checkbox
        // options == cycling, hiking, running, hunting
        // addition 'endurance' option for hardcore athletes
        // can add aditional options later and climate options like hot or cold climates
        // based on what the user selects it will filter by breed and it will only show adult and younger dogs
                // CURRENTLY -- does not only show adult or younger dogs
        location: '',
        // user enters zip or city and state
        // need results sorted by closest first
        // can later allow user to choose sort function
        pageNumber: 1,
        // the starting page number
        // equivalent to current_page in the json data

        // breedAdded: false,
        // I think I made this for interactivity in the drop down menu
        // switch this back and forth @change (clicking on the breed) which will change a - to a + or vice versa
        // and will highlight the selection if it is a +

        userBreeds: [],
        // when a user clicks on a breed it will be added here via a v-model
        // need to be in ["breed1", "breed2"] format
        // this is what is passed into the api call to petFinder

        activityBreeds: [],
        // when the activity is selected a method will go through the breedList and pull out the breeds for that activity and put it in here
        // these are the breeds (but only the breed part of it) that will be displayed in the dropdown
                // these Breeds can then be further sorted by the 'endurance' checkbox
                // if 'endurance' is selected the highlighted breeds will only be the endurance breeds
                // this is a feature I will add later
        // this variable MIGHT NOT BE NEEDED

        breedList: [],
        // fill this object with an api call from the internal api

        dogData: {},
        // for storing the data returned by the PetFinder api call of the different dogs

        // -------------------------------//

            // {breed: 'akita', activites: ['hiking', 'hunting', 'skiing'], endurance: false, id: 1}, // tested
            // {breed: 'alaskan malamute', activites: ['hiking', 'running', 'skiing'], endurance: true, id: 2}, //tested
            // {breed: 'american eskimo dog', activites: ['hiking'], endurance: false, id: 3}, // tested
            // {breed: 'american staffordshire terrier', activites: ['hiking'], endurance: false, id: 4}, // tested
            // // {breed: 'anatolian shephard', activites: ['hiking', 'running'], endurance: true}, // tested not working --
                    // NOT WORKING BREEDS -- I just need to get the petfinder api name for this breed and it should work
            // // {breed: 'australian cattle dog', activites: ['hiking', 'running'], endurance: true}, // tested not working
            // {breed: 'australian kelpie', activites: ['hiking', 'running'], endurance: true, id: 5}, // tested
            // // {breed: 'australian shephard', activites: ['hiking', 'running'], endurance: true}, // tested not working
            // {breed: 'labrador retriever', activities: ['hiking', 'hunting'], endurance: false, id: 6}, 
            // {breed: 'husky', activites: ['hiking', 'running', 'skiing'], endurance: true, id: 7}, // tested
            // {breed: 'golden retriever', activites: ['hiking', 'hunting'], endurance: false, id: 8}, // tested


        // endurance is not currently used but is added as something to be used in future
        // it can be an option for individuals such as marathon runners looking for dogs that can go the distance
        // given to dog breeds with extreme potential for athletic ability ONLY of course individual dogs will vary

        // ranking system -- > hiking -- considered on a more casual level (day hiker level)
                          // running -- more intense energy level than hiking
                          // hunting -- dog breeds that were designed for hunting
                                    // potential future categories -- retrieval, pointers, sight hounds, scent hounds
                          // skiing -- all the classic sled dog breeds + some other long haired breeds like akita
                                    // later add a 'mushing/pulling' for only the sled dog breeds?
                /// can also go through and look at pets listed under each breed to get a since of which breeds are more inclined for the 
                /// endurance attribute as most are mixes so the breeds are somewhat subjective
                /// also when ENDURANCE option checked senior dogs should be excluded from results
        
        // ------------------ //
    },
    methods: {

        getNewDogData: function() {
            this.pf.animal.search({
                type: "dog",
                breed: this.userBreeds,
                page: this.pageNumber,
                location: this.location,
                
                // breed: ["husky", "golden retriever"]
            }).then(response => {
                this.dogData = response.data
                for (let dog of this.dogData.animals) {
                    dog.distance = Math.floor(dog.distance)
                }
            })
            this.pageNumber = 1
        },
        
        getDogData: function() {
            this.pf.animal.search({
                type: "dog",
                breed: this.userBreeds,
                page: this.pageNumber,
                location: this.location,
                // breed: "husky"
            }).then(response => {
                this.dogData = response.data
            })
       },

       getBreedData: function() {
            axios({
                method: 'get',
                url: '/api/v1/activities/'
            }).then(response => {
                this.breedList = response.data
            })
       },

       sortBreedsByActivity: function() {

            activityBreeds = []
            for (let activity_object of this.breedList) {
                if (activity_object.activity === this.activity) {
                    for (let breed of activity_object.breed_detail) {
                        this.activityBreeds.push(breed)
                    }
                }
        }
        }, 

       nextPage: function() {
        this.pageNumber ++
        this.getDogData()
       },

       backPage: function() {
        this.pageNumber --
        this.getDogData()
       },

    //    activityType: function() {

    //    }

    },

    created: function() {
        this.getBreedData()
    },
})

// need to change userBreeds to an empty list and then have each breed added to the list when selected from drop down menu (using a v-model)

// this will be first step, if you have time later you can pull all dogs and then work with the data yourself

// TO DO TOMORROW
// then get the drop down menu working by creating a function that will run through the api and sort out breeds that fit that activity
// will need to use @change instead of @click and it will be a part of the select tab
// https://stackoverflow.com/questions/46260052/using-click-in-select-options-vue-js-2