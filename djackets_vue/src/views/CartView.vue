<template>
    <div class="page-cart">
        <div class="column is-12">
            <h1 class="title">Cart</h1>
        </div>

        <div class="columns is-12 box">
            <table class="table is-fullwidth" v-if="cartTotalLength">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>
                    <CartItem v-for="item in cart.items" v-bind:key="item.id" v-bind:item="item" />
                </tbody>
            </table>

            <p v-else>You don't have any products in your cart...</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import CartItem from '@/components/CartItem.vue';

    export default {
        name: 'CartView',
        components: {
            CartItem
        },
        data() {
            return {
                cart: {
                    items: []
                },
                isLoading: false,
                error: null,
            }
        },
        mounted() {
            this.cart = this.$store.state.cart
        },
        computed: {
            cartTotalLength() {
                return this.cart.items.reduce((acc, curVal) => acc + curVal.quantity, 0)
            },
            cartTotal() {
                let total = 0
                this.cart.items.forEach(item => {
                    total += item.quantity * item.product.price
                })
                return total
            }
        },
    }

</script>