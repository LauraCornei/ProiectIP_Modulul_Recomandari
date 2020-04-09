const data = [
    {
        id: 0,
        name: 'Restaurant Title1',
        img:
            'https://lh3.googleusercontent.com/VPWlDzu1I_v36IBv7d_dx4z5tnQZVHwCM5ZNOqriAGx13ZZlz0zTK7tMmgzLxjkPizewSA_mYUy8qcN8sg=w1080-h608-p-no-v0',
        description: 'Restaurant description',
    },
    {
        id: 1,
        name: 'Restaurant Title2',
        img:
            'https://cdn.homedit.com/wp-content/uploads/2016/06/Reds-True-Barbecue-building.jpg',
        description: 'Restaurant description',
    },
    {
        id: 2,
        name: 'Restaurant Title3',
        img:
            'https://res.cloudinary.com/culturemap-com/image/upload/ar_4:3,c_fill,g_faces:center,w_1200/v1548434789/photos/288737_original.jpg',
        description: 'Restaurant description',
    },
    {
        id: 3,
        name: 'Restaurant Title4',
        img:
            'https://media-cdn.tripadvisor.com/media/photo-s/11/af/e6/4a/hasienda-restaurant-outside.jpg',
        description: 'Restaurant description',
    },
    {
        id: 4,
        name: 'Restaurant Title5',
        img:
            'https://www.oradesibiu.ro/wp-content/uploads/2019/09/terasa-arini-hotel-parc_3.jpeg',
        description: 'Restaurant description',
    },
    {
        id: 5,
        name: 'Restaurant Title6',
        img:
            'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS4IT06ih0OBogC0Q4IIx-ethTIhhucncwvReLxQbsYbEaTSmt2&usqp=CAU',
        description: 'Restaurant description',
    },
];

const API_URL = 'http://localhost:5000/';

const MEDIA_BREAKPOINTS = {
    LG: 1500,
    MD: 780,
    SM: 420,
};

window.app = new Vue({
    el: '#app',
    data: {
        window: {
            width: 0,
            height: 0,
        },
        rawData: data,
        search: '',
        slide: 0,
        sliding: null,
    },
    
    computed: {
        carouselSections: function () {
            let cardsNo = 1;
            if (this.window.width > MEDIA_BREAKPOINTS.LG) cardsNo = 4;
            else if (this.window.width > MEDIA_BREAKPOINTS.MD) cardsNo = 3;
            else if (this.window.width > MEDIA_BREAKPOINTS.SM) cardsNo = 2;
            return _.chunk(this.rawData, cardsNo);
        },
    },

    mounted: function () {
        this.$nextTick(function () {
          this.getUserIdRecomendation();
        })
      },

    created() {
        window.addEventListener('resize', this.handleResize);
        this.handleResize();
    },
    destroyed() {
        window.removeEventListener('resize', this.handleResize);
    },

    methods: {
        async getUserIdRecomendation() {
            const recommendationsArray = await this.getRecommedations(getParamValue('user_id'));
            this.rawData = recommendationsArray;
        },

        getRecommedations(userId) {
            return fetch(
                `${API_URL}recommendations/restaurant/${userId}`
            ).then((res) => res.json());
        },

        handleResize() {
            this.window.width = window.innerWidth;
            this.window.height = window.innerHeight;
        },

        onSlideStart(slide) {
            this.sliding = true;
        },
        onSlideEnd(slide) {
            this.sliding = false;
        },
    },
});
