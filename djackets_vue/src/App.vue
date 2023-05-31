<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link class="navbar-item" to="/"><strong>Djackets</strong></router-link>
        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
          data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link class="navbar-item" to="/summer">Summer</router-link>
          <router-link class="navbar-item" to="/winter">Winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link class="button is-light" to="/login">
                <strong>Login</strong>
              </router-link>
              <router-link class="button is-success" to="/cart">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>

  <section class="section">
    <router-view />
  </section>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2023</p>
  </footer>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
