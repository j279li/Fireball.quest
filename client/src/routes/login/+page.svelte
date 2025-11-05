<!-- <script lang="ts">
    import { PUBLIC_BACKEND_BASE } from '$env/static/public';
    import { goto } from '$app/navigation';

    let failed = $state(false);

    async function submitForm(e: Event) {
        e.preventDefault();
        failed = false;
        const res = await fetch(PUBLIC_BACKEND_BASE + '/token', {
            method: "POST",
            body: new FormData(e.currentTarget)
        });
        if (res.ok) {
            const { access_token } = await res.json();
            localStorage.setItem('token', access_token);
            goto('/');
        } else failed = true;
    }
</script>
<form onsubmit={async e => {
    e.preventDefault();
    failed = false;
    const res = await fetch(PUBLIC_BACKEND_BASE + '/token', {
        method: "POST",
        body: new FormData(e.currentTarget)
    });
    if (res.ok) {
        const { access_token } = await res.json();
        localStorage.setItem('token', access_token);
        goto('/');
    } else failed = true;
}}>
    <label>
        Username:
        <input name="username" required />
    </label>
    <label>
        Password:
        <input type="password" name="password" required />
    </label>
    <button>Login</button>
</form>
{#if failed}
    <p style="color: red;">Login failed. Please try again.</p>
{/if} -->


<script lang="ts">
    import { PUBLIC_BACKEND_BASE } from '$env/static/public';
    import { goto } from '$app/navigation';
    import { Button } from "$lib/components/ui/button/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import { Input } from "$lib/components/ui/input/index.js";
    import * as Card from "$lib/components/ui/card/index.js";

    let failed = $state(false);
    let username = $state("");
    let password = $state("");

    async function handleLogin(e: Event) {
        e.preventDefault();
        failed = false;

        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const res = await fetch(PUBLIC_BACKEND_BASE + '/token', {
            method: "POST",
            body: formData,
        });

        if (res.ok) {
            const { access_token } = await res.json();
            localStorage.setItem('token', access_token);
            goto('/chat');
        } else failed = true;
    }
</script>

<div class="flex items-center justify-center bg-gray-100 flex-1">
    <Card.Root class="w-full max-w-sm">
        <Card.Header>
            <Card.Title>Login to your account</Card.Title>
            <Card.Description>
                Enter your username below to login to your account
            </Card.Description>
            <Card.Action>
                <Button variant="link" href="/signup">Sign Up</Button>
            </Card.Action>
        </Card.Header>

        <Card.Content>
            <form onsubmit={handleLogin} class="space-y-4">
                <div class="grid gap-2">
                    <Label for="username">Username</Label>
                    <Input
                        type="text"
                        placeholder="Enter username"
                        bind:value={username}
                        required
                        autofocus
                    />
                </div>

                <div class="grid gap-2">
                    <div class="flex items-center">
                        <Label for="password">Password</Label>
                        <a
                            href="/forgot-password"
                            class="ml-auto inline-block text-sm underline-offset-4 hover:underline"
                        >
                            Forgot your password?
                        </a>
                    </div>
                    <Input
                        type="password"
                        placeholder="Enter password"
                        bind:value={password}
                        onkeydown={(e) => {
                            e.key === 'Enter' && handleLogin(e)
                        }}
                        required
                    />
                </div>
            </form>
        </Card.Content>

        <Card.Footer class="flex-col gap-2">
            <Button type="submit" class="w-full" onclick={handleLogin}>Login</Button>
            {#if failed}
                <p class="text-sm text-red-600">Login failed. Please try again.</p>
            {/if}
        </Card.Footer>
    </Card.Root>
</div>