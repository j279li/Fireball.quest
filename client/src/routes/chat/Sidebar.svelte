<script lang="ts">
  import { ScrollArea } from "$lib/components/ui/scroll-area";
  import { Separator } from "$lib/components/ui/separator";
  import { Button } from "$lib/components/ui/button";
  import { page } from "$app/stores";

  $: path = $page.url.pathname;

  const links = [
    { href: "/chat",        label: "Character", icon: "👤" },
    { href: "/chat/spells", label: "Spells",    icon: "⚡" },
    { href: "/chat/items",  label: "Items",     icon: "📦" },
    { href: "/chat/notes",  label: "Notes",     icon: "📝" }
  ];

  const isActive = (href: string) =>
    href === "/chat" ? path === "/chat" : path.startsWith(href);
</script>

<div class="flex h-full flex-col">
  <!-- Header (fixed) -->
  <div class="p-4 pb-3 shrink-0">
    <a href="/sessions" class="inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground">
      ← <span>Back to Sessions</span>
    </a>
    <h1 class="mt-3 text-lg font-semibold leading-tight">
      The Sunless Citadel
      <span class="block text-sm font-normal text-muted-foreground">Session 3</span>
    </h1>
    <div class="mt-2 flex items-center gap-2">
      <span class="h-2.5 w-2.5 rounded-full bg-green-500"></span>
      <span class="text-sm text-muted-foreground">2 Online</span>
    </div>
  </div>

  <Separator class="shrink-0" />

  <!-- Scrollable body (nav + stats) -->
  <ScrollArea class="flex-1 min-h-0 px-2">
    <nav class="mt-3 space-y-1">
      {#each links as link}
        <a
          href={link.href}
          class={`flex items-center gap-2 rounded-md px-3 py-2 text-sm font-medium
                  ${isActive(link.href)
                    ? "bg-accent text-accent-foreground shadow-sm"
                    : "text-foreground/90 hover:bg-accent hover:text-accent-foreground"}`}
        >
          <span>{link.icon}</span>
          <span>{link.label}</span>
        </a>
      {/each}
    </nav>

    <Separator class="my-4" />

    <h2 class="px-3 text-sm font-medium text-muted-foreground">Character Stats</h2>

    <!-- Tightened cards to save vertical space -->
    <div class="p-3 space-y-2 text-sm">
      <div class="rounded-md border bg-background px-3 py-2">
        <p class="text-xs text-muted-foreground">Name</p>
        <p class="font-medium leading-tight">Thalen Brightblade</p>
      </div>

      <div class="rounded-md border bg-background px-3 py-2">
        <p class="text-xs text-muted-foreground">Class & Level</p>
        <p class="font-medium leading-tight">Half-Elf Ranger, Level 5</p>
      </div>

      <div class="grid grid-cols-3 gap-2">
        {#each [
          ["STR", 14, "+2"],
          ["DEX", 18, "+4"],
          ["CON", 16, "+3"],
          ["INT", 12, "+1"],
          ["WIS", 15, "+2"],
          ["CHA", 13, "+1"],
        ] as [stat, val, mod]}
          <div class="rounded-md border bg-background p-2 text-center leading-tight">
            <p class="text-[10px] text-muted-foreground">{stat}</p>
            <p class="text-base font-semibold">{val}</p>      <!-- was larger -->
            <p class="text-[10px] text-muted-foreground">{mod}</p>
          </div>
        {/each}
      </div>
    </div>
  </ScrollArea>

  <Separator class="shrink-0" />

  <!-- Footer (fixed) -->
  <div class="p-4 shrink-0">
    <Button class="w-full" variant="secondary">+ New Channel</Button>
  </div>
</div>
