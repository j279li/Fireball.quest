<script lang="ts">
  export let data;
  import Sidebar from "./Sidebar.svelte";
</script>

<!-- Full-height two-column layout -->
<div class="flex h-[90svh]">
  <!-- Left: sidebar -->
  <aside class="w-64 shrink-0 border-r bg-background">
    <Sidebar />
  </aside>

  <!-- Right: current /chat page -->
  <main class="flex-1 min-w-0 flex flex-col">
    <slot />
  </main>
</div>
