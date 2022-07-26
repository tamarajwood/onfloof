const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: "",
        postsList: [],
        // subjectsList: [],
        hikeList: [],
        bikeList: [],
        mushList: [],
    },
    methods: {

        loadSubjects: function() {
            console.log('cat')
            // console.log(this.postsList)
            for (let post of this.postsList) {
                for (let subject of post.subject_detail) {
                    if (subject.subject === "hiking") {
                        this.hikeList.push(post)
                    }
                    if (subject.subject === "cycling") {
                        this.bikeList.push(post)
                    }
                    if (subject.subject === "mushing") {
                        this.mushList.push(post)
                    }
                }
            }
            // this.postsList.forEach((value,index) =>{ 
            //     let subjectItem = value[0]
            //     if (subjectItem == 'hiking') {
            //         this.hikeList.unshift(post)
            //     }
            //     else if (subjectItem == 'cycling') {
            //         this.bikeList.unshift(post)
            //     }
            //     else if (subjectItem == 'mushing') {
            //         this.mushingList.unshift(post)
            //     }
            
        },

        loadPosts: function() {
            axios({
                method: 'get',
                url: '/api/v1/posts/'
            }).then(response => {
                this.postsList = response.data
                console.log(response.data)
                this.loadSubjects()
            })


        },

       
        // loadSubjects: function() {
        //     axios({
        //         method: 'get',
        //         url: '/api/v1/subjects/'
        //     }).then(response => this.subjectsList = response.data)
        // }, 
    },
       
    
    created: function() {
        this.loadPosts()
        // this.loadSubjects()
    },

    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})

    // mounted: function () {

    // }


        // this is causing an errpr but page still renders properly
        // do I not need a csrfToken or is this something I need to ask on how
        // to put into my vue app properly?
        // TypeError: Cannot read properties of null (reading 'value')
        // STILL GETTING ERROR EVEN AFTER COMMENT OUT
