<template>
    <div class="page-category">
        <div class="container">
            <div class="columns is-multiline">
                <div class="column is-3"
                v-for="product in category.products"
                v-bind:key="product.id"
                >
                <div class="box">
                  <figure class="image mb-4">
                    <img :src="product.get_thumbnail">
                  </figure>
            
                  <h3 class="is-size-4">{{ product.name }}</h3>
                  <p class="is-size-6 has-text-centered">{{ product.price }}</p>
                  <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">
                    View details
                  </router-link>
            
                </div>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
    name: 'CategoryView',
    data() {
        return {
            category: {
                products: []
            },
        }
    },
    mounted() {
        this.getCategory()
    },
    methods: {
        async getCategory() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug

            await axios.get(`/api/v1/categories/${category_slug}/`)
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