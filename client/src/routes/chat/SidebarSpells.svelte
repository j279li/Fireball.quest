<script lang="ts">
  import { Input } from "$lib/components/ui/input";
  import { Separator } from "$lib/components/ui/separator";
  import { Button } from "$lib/components/ui/button";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let slots: { level: number; total: number; used: number }[] = [
    { level: 1, total: 4, used: 1 },
    { level: 2, total: 2, used: 0 }
  ];
  export let prepared: { name: string; level: number }[] = [
    { name: "Hunter's Mark", level: 1 },
    { name: "Cure Wounds", level: 1 },
    { name: "Speak with Animals", level: 1 }
  ];

  let q = "";

  function inc(level: number) {
    const s = slots.find(x => x.level === level);
    if (!s || s.used >= s.total) return;
    s.used += 1;
    dispatch("slotsChange", { slots });
  }
  function dec(level: number) {
    const s = slots.find(x => x.level === level);
    if (!s || s.used <= 0) return;
    s.used -= 1;
    dispatch("slotsChange", { slots });
  }
  function removePrepared(i: number) {
    prepared.splice(i, 1);
    prepared = [...prepared];
    dispatch("preparedChange", { prepared });
  }

  $: filtered = q
    ? prepared.filter(p => p.name.toLowerCase().includes(q.trim().toLowerCase()))
    : prepared;
</script>

<h2 class="px-3 text-sm font-medium text-muted-foreground">Spells</h2>

<div class="p-3 space-y-3 text-sm">
  <div class="rounded-md border bg-background p-3">
    <div class="mb-2 flex items-center justify-between">
      <p class="text-xs text-muted-foreground">Spell Slots</p>
      <button
        type="button"
        class="text-xs text-muted-foreground hover:text-foreground"
        on:click={() => {
          slots = slots.map(s => ({ ...s, used: 0 }));
          dispatch("slotsChange", { slots });
        }}
      >
        reset
      </button>
    </div>

    <div class="space-y-2">
      {#each slots as s}
        <div class="flex items-center justify-between rounded-md border px-2 py-1.5">
          <div class="flex items-baseline gap-2">
            <span class="text-xs">Level {s.level}</span>
            <span class="text-xs text-muted-foreground">{s.used}/{s.total} used</span>
          </div>
          <div class="flex items-center gap-1">
            <Button variant="secondary" size="sm" class="h-6 px-2" on:click={() => dec(s.level)}>–</Button>
            <Button variant="secondary" size="sm" class="h-6 px-2" on:click={() => inc(s.level)}>+</Button>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <div class="rounded-md border bg-background p-2">
    <Input placeholder="Search prepared…" bind:value={q} class="h-8" />
  </div>

  <div class="rounded-md border bg-background p-3">
    <p class="mb-2 text-xs text-muted-foreground">Prepared</p>

    {#if filtered.length === 0}
      <p class="px-2 py-1 text-xs text-muted-foreground">No spells.</p>
    {:else}
      <ul class="space-y-1">
        {#each filtered as s, i}
          <li class="flex items-center justify-between rounded-md px-2 py-1 hover:bg-accent/50">
            <button
              type="button"
              class="truncate text-left"
              title={s.name}
              on:click={() => dispatch("openSpell", s)}
            >
              <span class="mr-2 text-[10px] text-muted-foreground">Lv {s.level}</span>
              <span class="font-medium">{s.name}</span>
            </button>

            <button
              type="button"
              class="rounded-md border px-2 py-0.5 text-xs text-muted-foreground hover:bg-accent hover:text-accent-foreground"
              on:click={() => removePrepared(i)}
              aria-label="Remove prepared spell"
              title="Remove"
            >
              remove
            </button>
          </li>
        {/each}
      </ul>
    {/if}
  </div>

  <div class="flex items-center justify-between">
    <span class="text-xs text-muted-foreground">Need another spell?</span>
    <Button size="sm" variant="secondary" class="h-7 px-2" on:click={() => dispatch("addSpell")}>
      + Add
    </Button>
  </div>
</div>

<Separator class="mt-3" />
