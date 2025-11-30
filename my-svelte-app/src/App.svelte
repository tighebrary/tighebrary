<svelte:options runes={true} />
<script>
  import data from './lib/data.json';
  
  let count = $state(0);

  let match = $derived(data.find(d => d.presses === count));
  
  let buttonLabel = $state('');
  $effect(() => {
    if (match) {
      buttonLabel = match.text;
    }
  });
  
  function increment() {
    count += 1
  }
</script>

<main>
  <div>
    <button onclick={increment}>
      {buttonLabel}
    </button>
  </div>
</main>

<style>
    main {
    font-family: sans-serif;
    text-align: center;
    margin-top: 50px;
  }

  button {
    font-size: 1.5rem;
    padding: 1rem 2rem;
    cursor: pointer;
    background-color: #ff3e00;
    color: white;
    border-color: #ff3e00;
    border: 2px solid #ccc;
    border-radius: 8px;
    transition: all 0.2s;
    user-select: none;
    white-space: pre-wrap; 
  }

  @keyframes fade {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
