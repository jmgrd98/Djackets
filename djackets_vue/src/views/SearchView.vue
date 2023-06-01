<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
            </div>

            <ProductBox v-for="product in products" v-bind:key="product.id" v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue';

export default {
    name: 'SearchView',
    components: {
        ProductBox
    },
    data() {
        return {
            products: [],
            query: '',
            error: null,
        }
    },
    mounted() {
        document.title = 'Search'
        this.getProducts()
    },
}

</script>