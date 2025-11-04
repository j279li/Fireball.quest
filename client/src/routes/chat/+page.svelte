<script lang="ts">
    import { PUBLIC_BACKEND_BASE } from "$env/static/public";
    import { onMount } from "svelte";

    let ws: WebSocket;
    let messages: {username: string, message: string}[] = $state([]);
    onMount(() => {
        ws = new WebSocket(PUBLIC_BACKEND_BASE.replace(/^http/, 'ws') + '/chat/test?token=' + localStorage.getItem('token'));
        ws.onmessage = event => {
            messages = [...messages, JSON.parse(event.data)];
        };
    });
    let text = $state('');
</script>
<h1>Chat</h1>
<div>
{#each messages as msg}
    <p><strong>{msg.username}:</strong> {msg.message}</p>
{/each}
</div>
<form onsubmit={e => {
    e.preventDefault();
    ws.send(text);
    text = '';
}}>
    <textarea bind:value={text}></textarea>
    <button type="submit">Send</button>
</form>
