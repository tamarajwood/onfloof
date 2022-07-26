const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: "",
        postsList: [],
        hikeList: [],
        bikeList: [],
        mushList: [],
    },
    methods: {
        loadPosts: function() {
            axios({
                method: 'get',
                url: '/api/v1/posts/'
            }).then(response => this.postsList = response.data)
        },
        loadSubjects: function() {
            console.log('cat')
            this.postsList.forEach((value,index) =>{ 
                let subjectItem = value[0]
                if (subjectItem == 'hiking') {
                    this.hikeList.unshift(post)
                }
                else if (subjectItem == 'cycling') {
                    this.bikeList.unshift(post)
                }
                else if (subjectItem == 'mushing') {
                    this.mushingList.unshift(post)
                }
            console.log('dog')
                })
        }, 
    },
       
    
    created: function() {
        this.loadPosts(),
        this.loadSubjects()
    },
})

    // mounted: function() {
    //     this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
        // this is causing an errpr but page still renders properly
        // do I not need a csrfToken or is this something I need to ask on how
        // to put into my vue app properly?
        // TypeError: Cannot read properties of null (reading 'value')
        // STILL GETTING ERROR EVEN AFTER COMMENT OUT
