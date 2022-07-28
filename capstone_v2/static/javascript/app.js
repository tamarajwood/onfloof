const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: "",
        postsList: [],
        hikeList: [],
        bikeList: [],
        mushList: [],
        currentPost: {},
    },
    methods: {

        loadSubjects: function() {
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
            
        },

        loadPosts: function() {
            axios({
                method: 'get',
                url: '/api/v1/posts/'
            }).then(response => {
                this.postsList = response.data
                this.loadSubjects()
                this.loadCurrentPost()
            })


        },

        loadCurrentPost: function() {
            let postId = window.location.pathname
            postId = parseInt(postId.substring(1, postId.length-1))

            for (let post of this.postsList) {
                if (post.id === postId) {
                    this.currentPost = post
                    // this.currentPost.push(post)
                }
            }
        }

    },
       
    
    created: function() {
        this.loadPosts()
    },

    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})
