<template>
  <b-container>
    <b-list-group>
      <b-list-group-item v-for="puppy in puppies" :key="puppy.id">
        <b-row>
          <b-col>{{ puppy.name }} ({{ puppy.breed }})</b-col>
          <b-col class="text-right">
            <b-button variant="success" @click="adoptPuppy(puppy.id)">Adopt</b-button>
          </b-col>
        </b-row>
      </b-list-group-item>
    </b-list-group>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      puppies: []
    }
  },
  mounted() {
    this.fetchPuppies();
  },
  methods: {
    async fetchPuppies() {
      const response = await fetch('http://localhost:5000/puppies');
      const data = await response.json();
      this.puppies = data;
    },
    async adoptPuppy(id) {
      const response = await fetch(`http://localhost:5000/puppy/adopt/${id}`, {
        method: 'PUT'
      });
      if (response.ok) {
        this.fetchPuppies();
        alert('Puppy adopted successfully!');
      } else {
        alert('Failed to adopt puppy');
      }
    }
  }
}
</script>
