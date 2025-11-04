<script lang="ts">
    import { PUBLIC_BACKEND_BASE } from '$env/static/public';
    import { goto } from '$app/navigation';

    let failed = $state(false);
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
{/if}
