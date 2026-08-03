const CACHE_NAME = "novacore-v1";

const urlsToCache = [
    "/",
    "/static/css/style.css",
    "/static/js/app.js",
    "/static/assets/icons/novacore_icon.png"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
