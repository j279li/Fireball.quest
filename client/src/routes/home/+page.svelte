<script lang="ts">
  	import { Button } from "$lib/components/ui/button";
	import { goto } from '$app/navigation';
</script>

<div class="flex flex-col flex-1 items-center justify-center p-6 gap-4 bg-gray-50">
	<!-- App Title -->
	<h1 class="text-2xl font-bold text-red-600 text-center">Welcome to Fireball.quest</h1>

	<!-- Description -->
	<p class="text-gray-600 text-lg max-w-xl text-center">
		Max is slacking.
	</p>

	<!-- Navigation buttons -->
	<div class="flex gap-4">
		<Button variant="outline" onclick={() => goto('/chat')}>Chat</Button>
		<Button variant="outline" onclick={() => goto('/login')}>Login</Button>
	</div>
</div>