function scrapBundle() {
  let newBundle = new ObjectMap();
  Core.bundle.keys.forEach((k) => {
    newBundle.put(k, k);
  });
  Core.bundle.setProperties(newBundle);
}

Events.on(ClientLoadEvent, scrapBundle);
