import { redirect } from '@sveltejs/kit';

// REDIRECT BASE URL TO /home

export function load() {
    throw redirect(307, '/home'); // temporary redirect
}
