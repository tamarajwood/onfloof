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

        commentMode: false,
        comment: {
            comment: '',
            post: []
        },
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
                for (let post of this.postsList) {
                    post.created = post.created.substring(0, 10)
                    for (let comment of post.comment_detail) {
                        comment.created = comment.created.substring(0, 10)
                    }
                }
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
        },

        // currentDate: function() {
        //     let currentDate = new Date()
        //     let currentDay = currentDate.getDate()
        //     let currentMonth = currentDate.getMonth() + 1
        //     let currentYear = currentDate.getFullYear()
        //     let created = `${currentDay}/${currentMonth}/${currentYear}`
        //     return created
        // },

        postComment: function() {

            this.comment.post.push(this.currentPost.id)
            // console.log(this.comment)
            console.log(this.currentPost.id)
            console.log(this.comment)

            axios({
                method: 'post',
                url: '/api/v1/comments/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: this.comment
            }).then(response => {
                this.loadPosts()
                this.comment = {
                    comment: '',
                    post: [this.currentPost.id]
                }
            })
        }

    },
       
    
    created: function() {
        this.loadPosts()
    },

    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})
