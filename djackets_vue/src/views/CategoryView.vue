<template>
    <div class="page-category">
        <div class="column is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    {{ category.name }}
                </h2>
            </div>

            <ProductBox v-for="product in category.products" v-bind:key="product.id" v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import ProductBox from '@/components/ProductBox.vue';

export default {
    name: 'CategoryView',
    data() {
        return {
            category: {
                products: []
            },
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        '$route'(to, from) {
            if (to.name == 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug

            await axios.get(`/api/v1/products/${category_slug}/`)
                .then(response => {
                    this.category = response.data;
                    document.title = this.category.name + ' | Djackets'
                })
                .catch(error => {
                    this.error = error;

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true
                    })
                })

            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>