<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>{{ item.quantity }}</td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete"></button></td>
    </tr>
</template>

<script>

export default {
    name: 'CartItem',
    props: {
        initialItem: Object,
    },
    data() {
        return {
            item: this.initialItem,
            isLoading: false,
            error: null,
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        async decrementQuantity() {
            if (this.item.quantity > 1) {
                this.item.quantity--
                await this.updateItem()
            }
        },
        async incrementQuantity() {
            this.item.quantity++
            await this.updateItem()
        },
        async updateItem() {
            this.isLoading = true
            await axios.put(`/api/v1/cart/items/${this.item.id}/`, this.item)
                .then(response => {
                    this.item = response.data
                })
                .catch(error => {
                    this.error = error
                })
            this.isLoading = false
        },
        async removeItem() {
            this.isLoading = true
            await axios.delete(`/api/v1/cart/items/${this.item.id}/`)
                .then(response => {
                    this.$store.commit('removeItemFromCart', this.item)
                })
                .catch(error => {
                    this.error = error
                })
            this.isLoading = false
        },
    }
}

</script>