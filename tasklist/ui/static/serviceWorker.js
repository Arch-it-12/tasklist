const staticTasklist = "jakes-ice-cream-tasklist-v1"
const assets = [
    "/",
    "../templates/",
    "/style.css",
    "/js/script.js",
    "/icecream.webp",
    "../templates/admin_panel.html",
    "../templates/base.html",
    "../templates/home.html",
    "../templates/tasks.html",
    "../templates/user_list.html"
]

self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticTasklist).then(cache => {
            cache.addAll(assets)
        })
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        })
    )
})