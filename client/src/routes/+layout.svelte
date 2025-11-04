<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Button from "$lib/components/ui/button/button.svelte";
	
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<!-- NAV BAR -->
<nav class="border-b border-gray-200 bg-white p-4 flex gap-4">
  <a href="/" class="font-semibold">Home</a>
  <a href="/chat">Chat</a>
</nav>

{@render children?.()}
