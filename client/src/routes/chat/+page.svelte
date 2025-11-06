<script lang="ts">
  import { PUBLIC_BACKEND_BASE } from "$env/static/public";
  import Button from "$lib/components/ui/button/button.svelte";
  import Input from "$lib/components/ui/input/input.svelte";
  import MessageItem from "./MessageItem.svelte";
  import { onMount, onDestroy, tick } from "svelte";

  // incoming message shape from the server (extend as you add fields)
  type WireMsg = {
    username: string;
    message: string;
    avatarUrl?: string;
    tag?: string;     // e.g., "Roll" | "OOC" | "Action"
    ts?: number;      // epoch ms from server (optional)
  };

  let ws: WebSocket;
  let scroller: HTMLDivElement;

  // local state (Svelte 5 runes)
  let messages = $state<
    Array<
      Required<Pick<WireMsg, "username" | "message">> & {
        avatarUrl?: string;
        tag?: string;
        ts: number;
      }
    >
  >([]);

  let text = $state("");

  onMount(() => {
    ws = new WebSocket(
      PUBLIC_BACKEND_BASE.replace(/^http/, "ws") +
        "/chat/test?token=" +
        localStorage.getItem("token")
    );

    ws.onmessage = (event) => {
      const m: WireMsg = JSON.parse(event.data);
      messages = [
        ...messages,
        {
          username: m.username,
          message: m.message,
          avatarUrl: m.avatarUrl,
          tag: m.tag,
          ts: m.ts ?? Date.now()
        }
      ];
    };

    ws.onerror = () => {
      console.error("WebSocket error");
    };
  });

  onDestroy(() => {
    if (ws && ws.readyState === WebSocket.OPEN) ws.close();
  });

  function sendMessage() {
    const payload = text.trim();
    if (!payload) return;
    if (ws?.readyState === WebSocket.OPEN) {
      ws.send(payload);
      text = "";
    }
  }

  // Auto-scroll when messages change (runes-mode safe)
  $effect(() => {
    // establish dependency
    void messages.length;
    // wait for DOM paint then scroll
    tick().then(() => {
      if (scroller) scroller.scrollTop = scroller.scrollHeight;
    });
  });
</script>

<div class="flex flex-col flex-1 p-6">
  <h1 class="text-2xl font-semibold mb-4 shrink-0">Global Chat</h1>

  <div class="flex flex-col gap-3 flex-1">
    <!-- Messages panel -->
    <div
      bind:this={scroller}
      class="flex-1 overflow-y-auto rounded-lg border bg-muted/30 p-4"
    >
      <ul class="space-y-4">
        {#each messages as m (m.ts + m.username + m.message)}
          <MessageItem
            username={m.username}
            message={m.message}
            avatarUrl={m.avatarUrl}
            tag={m.tag}
            ts={m.ts}
          />
        {/each}
      </ul>
    </div>

    <!-- Composer -->
    <form
      class="flex w-full items-center gap-2 shrink-0"
      on:submit|preventDefault={sendMessage}
    >
      <Input
        bind:value={text}
        placeholder="Type a message..."
        on:keydown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
          }
        }}
        autofocus
      />
      <Button type="submit">Send</Button>
    </form>
  </div>
</div>
