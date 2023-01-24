const staticTasklist = "jakes-ice-cream-tasklist-v1"
const assets = [
    "/",
    "/tasklist/ui/templates/",
    "/tasklist/ui/static/style.css",
    "/tasklist/ui/static/js/script.js",
    "/tasklist/ui/static/icecream.webp",
    "/tasklist/ui/templates/admin_panel.html",
    "/tasklist/ui/templates/base.html",
    "/tasklist/ui/templates/home.html",
    "/tasklist/ui/templates/tasks.html",
    "/tasklist/ui/templates/user_list.html"
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