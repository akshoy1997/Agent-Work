// var staticCacheName = 'djangopwa-v1';

this.addEventListener('fetch', function(event){
  event.respondWith(networkOrCache(event.request));
});

function networkOrCache(request){
  return fetch(request).catch(function(){
    return fromCache(request);
  });
}

function fromCache(request){
  return caches.open('djangopwa-v1').then(function(cache){
    return cache.match(request).then(function(matching){
      return matching;
    })
  })
}