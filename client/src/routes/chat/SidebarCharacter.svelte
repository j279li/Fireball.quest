<script lang="ts">
  export let name = "Thalen Brightblade";
  export let cls  = "Half-Elf Ranger, Level 5";
  export let stats: Array<[string, number, string]> = [
    ["STR", 14, "+2"], ["DEX", 18, "+4"], ["CON", 16, "+3"],
    ["INT", 12, "+1"], ["WIS", 15, "+2"], ["CHA", 13, "+1"],
  ];
</script>

<h2 class="px-3 text-sm font-medium text-muted-foreground">Character Stats</h2>

<div class="p-3 space-y-2 text-sm">
  <div class="rounded-md border bg-background px-3 py-2">
    <p class="text-xs text-muted-foreground">Name</p>
    <p class="font-medium leading-tight">{name}</p>
  </div>

  <div class="rounded-md border bg-background px-3 py-2">
    <p class="text-xs text-muted-foreground">Class & Level</p>
    <p class="font-medium leading-tight">{cls}</p>
  </div>

  <div class="grid grid-cols-3 gap-2">
    {#each stats as [stat, val, mod]}
      <div class="rounded-md border bg-background p-2 text-center leading-tight">
        <p class="text-[10px] text-muted-foreground">{stat}</p>
        <p class="text-base font-semibold">{val}</p>
        <p class="text-[10px] text-muted-foreground">{mod}</p>
      </div>
    {/each}
  </div>
</div>
