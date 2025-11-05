<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Button from "$lib/components/ui/button/button.svelte";
	import { page } from "$app/state";
	
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="flex flex-col min-h-screen">
	<!-- NAV BAR -->
	<nav class="border-b border-gray-200 bg-white p-4 flex gap-4">
		<a href="/" class="font-semibold" class:underline={page.url.pathname === '/home'}>Home</a>
		<a href="/chat" class="font-semibold" class:underline={page.url.pathname === '/chat'}>Chat</a>
		<a href="/login" class="font-semibold" class:underline={page.url.pathname === '/login'}>Login</a>
	</nav>

	
	{@render children?.()}
</div>