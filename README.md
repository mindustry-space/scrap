# scrap

Scrap is a Mindustry mod that sets all bundle values to their keys. It is useful when scraping data using [Pulverizer](https://github.com/mindustry-space/Pulverizer).

The bundles are generated using [generate.py](generate.py) which uses [bundle data](https://github.com/mindustry-space/lead/tree/main/bundles) collected from every release. I have to generate these bundles externally as I can't find a way that changes the bundles early enough that it affects the values present in the game's content. The only limitation of this method is that bleeding edge builds and mods may have keys that aren't updated.

## Installation

Scrap can be installed using the game's built-in mod browser.

You can also install it manually by [downloading this repository](https://github.com/mindustry-space/scrap/archive/refs/heads/main.zip) and saving it to your mods folder.

```sh
curl -L https://github.com/mindustry-space/scrap/archive/refs/heads/main.zip > ~/.local/share/Mindustry/mods/scrap.zip
```

## Usage

With the mod installed, all localised strings for all languages will be set to their bundle keys. For example, you'll notice that the database now looks something like this:

![](screenshot.png)

## License

[GPL-3.0](LICENSE)
