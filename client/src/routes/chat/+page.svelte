<script lang="ts">
    import { PUBLIC_BACKEND_BASE } from "$env/static/public";
    import Button from "$lib/components/ui/button/button.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
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

    function sendMessage() {
        if (text.trim()) {
            ws.send(text);
            text = "";
        }
    }
</script>

<div class="flex flex-col flex-1 p-6">
    <h1 class="text-2xl font-semibold mb-4">Global Chat</h1>

    <div class="flex flex-col gap-3 flex-1">
        <div class="border rounded-lg p-3 flex-1 overflow-y-auto bg-gray-50">
            {#each messages as msg (msg)}
                <span class="text-gray-700">{msg.username}</span> : <span class="text-gray-900">{msg.message}</span><br>
            {/each}
        </div>

        <form class="flex w-full items-center space-x-2">
            <Input
                bind:value={text}
                placeholder="Type a message..."
                onkeydown={(e) => {
                    e.key === 'Enter' && sendMessage()
                }}
                autofocus
            />
            <Button onclick={sendMessage}>Send</Button>
        </form>
    </div>
</div>
