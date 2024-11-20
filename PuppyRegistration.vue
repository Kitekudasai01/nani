<template>
  <b-container>
    <b-form @submit.prevent="registerPuppy">
      <b-form-group label="Puppy Name">
        <b-form-input v-model="name" required></b-form-input>
      </b-form-group>
      <b-form-group label="Breed">
        <b-form-input v-model="breed" required></b-form-input>
      </b-form-group>
      <b-form-group label="Age">
        <b-form-input v-model="age" type="number" required></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Register Puppy</b-button>
    </b-form>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      breed: '',
      age: null
    }
  },
  methods: {
    async registerPuppy() {
      const response = await fetch('http://localhost:5000/puppies', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: this.name,
          breed: this.breed,
          age: this.age
        })
      });
      if (response.ok) {
        alert('Puppy registered successfully!');
        this.name = '';
        this.breed = '';
        this.age = null;
      } else {
        alert('Failed to register puppy');
      }
    }
  }
}
</script>
