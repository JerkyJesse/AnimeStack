# Asset review manifest

Every picture under `art/` and `assets/` is named here once, with its hash. The
manifest is machine-checked by `scripts/check-leak` (`manifest_pass`): a shipped
picture with no row fails, a row whose sha256 does not match the file fails, a row
that names no file fails, and a verdict outside `PASS` / `HOLD` / `UNREVIEWED`
fails. Coverage and hashes are facts.

The review itself is human. No text gate reads pixels: a wordmark, a name, a path, a
ticker, a money figure, or a channel burned into a render is invisible to every scanner
in this repo. A reviewer opens the picture, looks for anything that names the private
reference or a live book, and records one verdict.

| Verdict | Means | Release effect |
| --- | --- | --- |
| `PASS` | A reviewer opened the file and found nothing private in it. | clears |
| `HOLD` | A reviewer opened the file and found something to resolve. | the release run fails until the chair resolves it |
| `UNREVIEWED` | The file is hashed and covered, and no reviewer has opened it yet. | named in the release run, never counted as a pass |

`UNREVIEWED` is not a pass and is never reported as one. A new or regenerated picture
takes its row and its hash in the same commit as the file; a changed hash with an
unchanged verdict is a review that did not happen.

At v2.0.0 the art set was re-rendered clean and then re-rendered again for the visual
pass: the private-stamped HUD and money copy are gone, the remaining character art is
cropped clean, and every card carries only public house text. The chair opened the set
and signs the pass.

## The table

One row per picture under `art/` and `assets/`, excluding directory READMEs.

| File | sha256 | Reviewer | Date | Verdict |
| --- | --- | --- | --- | --- |
| `art/dossiers/aria.jpg` | `68d833b7fd960591b2035a9af78cc7f0033ab1749f07dc3f0de2b73a168df06c` | Reika | 2026-11-05 | PASS |
| `art/dossiers/elo.jpg` | `fd5596483926305c5a221dee15fdde0f9e36dced5b7960d5e47ed840cf7bbfb7` | Reika | 2026-11-05 | PASS |
| `art/dossiers/mechapip.jpg` | `c4ed5d86eec711bbb0f7f4f1722ec4828ee2e3ff135f2c089e88e5f6006dd121` | Reika | 2026-11-05 | PASS |
| `art/dossiers/mei.jpg` | `ce52f10fff33b1eccfa838cce2b80a72b27ce159cb841b2d4a4f4c7f0a518538` | Reika | 2026-11-05 | PASS |
| `art/dossiers/niko.jpg` | `46a1b8805bd409ba3c82024ffdcf6b1f94f06bf78bdfc7f3e827da3f64798ea2` | Reika | 2026-11-05 | PASS |
| `art/dossiers/reika.jpg` | `3751de838929f1eef9699da1c7d744859123bc7a8b6fb9eecfada8cf4d0b6c80` | Reika | 2026-11-05 | PASS |
| `art/dossiers/rin.jpg` | `eea1f55ddd2b3c3866f3c8b9ea89c4b78b470e1565e487d288fc1e5a739c89d0` | Reika | 2026-11-05 | PASS |
| `art/dossiers/yui.jpg` | `f7e087a26868ac6f7e325894fd84be8f2554e2fb2d0097682c2f75d63d385b88` | Reika | 2026-11-05 | PASS |
| `art/sheets/aria-sheet-1.jpg` | `f7817fdc7295e5ca130f9eb34c7d01695f06a76aa5bcca07f824cb426106e32f` | Reika | 2026-11-05 | PASS |
| `art/sheets/elo-sheet-1.jpg` | `87b06971f5b15ba73a7181deb218c587ac766746cdae13e5dc78c87fc0d773dd` | Reika | 2026-11-05 | PASS |
| `art/sheets/mechapip-sheet-1.jpg` | `34d652194c6350bc29d1c387078173358ca850c207f68935c62c2b9eeb705b33` | Reika | 2026-11-05 | PASS |
| `art/sheets/mei-sheet-1.jpg` | `aba13d9217b25f616f37bddd06278bf5eb8c6681ff9053a151450f312141e0b5` | Reika | 2026-11-05 | PASS |
| `art/sheets/niko-sheet-1.jpg` | `7e264e70b7078d718c5b7496837cb722904ff96920bffe30b54f5a5aee83dd5d` | Reika | 2026-11-05 | PASS |
| `art/sheets/reika-sheet-1.jpg` | `0a7ee50ee9ca1c5c2d921f5f8272c344faed0a08fc0a0666556166a0a5242e2e` | Reika | 2026-11-05 | PASS |
| `art/sheets/rin-sheet-1.jpg` | `0d5eabb1dcf7c175767e8bb29593fe7949136e2ef89c1dd522783b2b61da7671` | Reika | 2026-11-05 | PASS |
| `art/sheets/yui-sheet-1.jpg` | `0dc14b7ef79441b12899491e631d3d6afc22183d220d624555a885c6963a0f8b` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/aria-stamped.jpg` | `0e8c75970eb192e18c36bc7a48bb52d983991227cd9054b713064b5986bb164f` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/elo-stamped.jpg` | `786c1ef7713b88d76dc2c524578468bd61c852b0d829e78e72c7aa11d0773559` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/mechapip-stamped.jpg` | `5501f92ef593ca67918ae4839b5a871ac5a3ee6895674bfba095b35a1f0c0220` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/mei-stamped.jpg` | `2a4eec2b47b5e8f2d83b46323cb0572902d98d6a90e3cab8aa5eb9a01d1596f4` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/niko-stamped.jpg` | `7c757e9766e9d0f7db7b4fe9e019e164ccb48a122ae78343a27e4fbe62d44066` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/reika-stamped.jpg` | `e39f15a2caad612c610107c8eb0e74b376b60f4907d457921a46334f0458eae0` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/rin-stamped.jpg` | `016e997895ad78ae4473e9d05db2dac9823883a1e442666332e7c3d8d6fbd975` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/yui-stamped.jpg` | `9d912d419f7740239b2509738de91b2203437c3e723b09c6db5dc7c4e4f1e8a6` | Reika | 2026-11-05 | PASS |
| `assets/img/aria-portrait.jpg` | `5af6672568f229ac3116e5fd09273f2b3c8044df245cbcdfc4982a084bf1758c` | Reika | 2026-11-05 | PASS |
| `assets/img/aria-roster.jpg` | `78d8819475a1eccdec518b97548109a93246e04160a7d9aba6c86f91c59540fb` | Reika | 2026-11-05 | PASS |
| `assets/img/elo-portrait.jpg` | `2c565347e56708027685ca6da23fc6060cc2df717d91a26bc901fc7df8bd9ca9` | Reika | 2026-11-05 | PASS |
| `assets/img/elo-roster.jpg` | `83cddd77accddf32aecb68e11b80e6c5ea57d03f9eeb3605dbf0c03bbcb689d6` | Reika | 2026-11-05 | PASS |
| `assets/img/hero-lineup.jpg` | `db5eba03ceaa2f0badc8bf279460c5526ab5f76b14ef6c8d49f011991fdaadd8` | Reika | 2026-11-05 | PASS |
| `assets/img/mechapip-portrait.jpg` | `f6adac646e340f725419d1ca6cb05e5f3482517a8ec7600f26c4c40d9d0cc560` | Reika | 2026-11-05 | PASS |
| `assets/img/mechapip-roster.jpg` | `6bc09c4275215609948270c66eeda1fc4fe229f4a892947416742e80b6b94120` | Reika | 2026-11-05 | PASS |
| `assets/img/mei-portrait.jpg` | `c0f1ae7b2fbb04b981658243f52e3c541e08c27f8825509c465b87d869649e8b` | Reika | 2026-11-05 | PASS |
| `assets/img/mei-roster.jpg` | `c7d45c6b47345cb4f1b52c468869a5e1123e9504d1044e844ef9fcde764f06e3` | Reika | 2026-11-05 | PASS |
| `assets/img/niko-portrait.jpg` | `3602fae164395aad6e157af9d30388c45b754cc393e2953ba99737e59db2e5e1` | Reika | 2026-11-05 | PASS |
| `assets/img/niko-roster.jpg` | `f6ab453be21cba2e7aeff9dcb20516868e076bc622761f935e3740ab6a53d408` | Reika | 2026-11-05 | PASS |
| `assets/img/reika-portrait.jpg` | `d9ecf15dce9b5e96487c00fb7d1e3d20ea9028828cb1cb55295b9ad1b9c5c26c` | Reika | 2026-11-05 | PASS |
| `assets/img/reika-roster.jpg` | `a2b7ca3b6923aa999a06d592645c1c7f493229973240370cbce38ac1c48ad346` | Reika | 2026-11-05 | PASS |
| `assets/img/rin-portrait.jpg` | `45139136974ffab1806574ddd82001fd1fee2ec3fbf1aee5b3d538573707a3b1` | Reika | 2026-11-05 | PASS |
| `assets/img/rin-roster.jpg` | `f1bd2c85d3513ccdd54eacd34eb4871778093e138a51ca6b82f2f09e66f5254e` | Reika | 2026-11-05 | PASS |
| `assets/img/social-preview.jpg` | `7467acea5b1fe107e5fa7123ec3d04f1c817562e791e4fea6a336b0e4c486086` | Reika | 2026-11-05 | PASS |
| `assets/img/team-composite.jpg` | `e8b8631c75181c24d670335e37e7a3a02fa68ad8266d402935b738b1184f1b0e` | Reika | 2026-11-05 | PASS |
| `assets/img/yui-portrait.jpg` | `ac817ced8c4099b098f899ceb5ee3a7398cadf59885db56d31a6a3889f600716` | Reika | 2026-11-05 | PASS |
| `assets/img/yui-roster.jpg` | `40600a30604a87df1a2ccd274d47c004fcec2bc0861b674d4379bf9a3f476a0a` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/aria.jpg` | `cc38ace486f20d81b11c45c925c23c85e43f13c64c40811575c8b3feeeb7ba50` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/elo.jpg` | `7e841907b6206d8b83f642e30dfdb38abf59bee0ee03b4f464176f94732bfe09` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/mechapip.jpg` | `2bf50c648276ac80875029193c35aaeab7d5804e8d570c17d077f13215b548c8` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/mei.jpg` | `632cd7ab367826aa9164a245755401b1e009b201daa7a4af2f416b59b43aa7c3` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/niko.jpg` | `f48eaa782b2ab02333c74430ab6c585bbfa38c566d1bf62f137f9b628f33451b` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/reika.jpg` | `5b3687314d55acea23084c99fa56614af641013f82cf52565e8fa6de6a4a45dc` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/rin.jpg` | `4618eeb4b5b7f5b4ae00671fed2c89b2c83c0b17876958d625750dd7e55db137` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/yui.jpg` | `8b90bbf8b51fdeda7c98e4b7f68430f7f7c54fd32fde7192e130a0e159a6c04d` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/aria.jpg` | `8b516ddcd303cb9f9293d9e738597038831fdd5d5241234cc430efd80d96dc83` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/elo.jpg` | `b2123b5c5de3bf6a1cd4993dcaa556d626788acd5a15b24dacc1b6ec645eda00` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/mechapip.jpg` | `39b1670e10df02aa3dfeffa7bd6ffd06322903d3450756fb6621a295b11cd6c9` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/mei.jpg` | `57915cbdbd466b0a263d0d50df3e517454672c9133d4193b6c8b47926e7e2614` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/niko.jpg` | `44a130d84a5c8e39780c721989b325d664441e74a6d3ef2945dc6c0eda4faebc` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/reika.jpg` | `4df8066bafd43c6d6cc91a8411d070f1bda7787a16faac97484421c34e5a2eff` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/rin.jpg` | `696df23e568fa8b62324cf1d6a04b34ff9a03af46d98a31210a6a5a1978d4f41` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/yui.jpg` | `69f36440d6df024eef67968c6cb748c7d6f87b16f325ed91a8301b219686a079` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/aria-sheet-1.jpg` | `25af3b227efb8e1e0af78895b63c388a45c61655b12989518505321540ff1a84` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/elo-sheet-1.jpg` | `b00d2430f2ca0e12b1e8b822fcd49b9e5459a28672ad8bd615f77f29faea5191` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/mechapip-sheet-1.jpg` | `30d28f363e5129f7a0135d3e0ed1f1234e8714ad4fbfdd92b4454f5f6132b3e0` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/mei-sheet-1.jpg` | `9277d11ce150e81739a6efbcc274575c1fddc879a856e41c29e329d09ed94b05` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/niko-sheet-1.jpg` | `974bb9060ece48a044dc2eb2c31847c4eed7e4c74f3a97e76a5b0b93c86ab56e` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/reika-sheet-1.jpg` | `483e8f4851d33b55aa151870c9e9e2c905eccd8fa6595c431e4149a9fbb82988` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/rin-sheet-1.jpg` | `80c4047d7fce62ecee684559aa2fbec538637dc2e15a54ff3ccc93c1d8c43aac` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/yui-sheet-1.jpg` | `602c2d8a38a34ae45f302a60b2710b96bbc380ec201dbfd7611982eed41c8fa4` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/aria-stamped.jpg` | `d0913b8035caefeb6d3a3cd40a9fbc486dc20aac7c25f188ce316a6465f588b0` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/elo-stamped.jpg` | `152c57ad495c6ae989fdc1e9c95e0e617ffdb0f1cd52ce49bf695023ac3f26f7` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/mechapip-stamped.jpg` | `3cf780e3325aa9bad7971d7c3ec265c3da11d6c21e7542dd6854d39edfeff9d4` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/mei-stamped.jpg` | `d9e70bb07594674357824a8bea447bc8280289ec765e4759188591fd03832733` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/niko-stamped.jpg` | `1e6e0a2d736901a4c37c532aadf1b5c4d5e9346655c7d9b66d3cfcbb08560811` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/reika-stamped.jpg` | `7399e62e84eb4c8efb0ba7816c3aa1bbf98ee1fa29f4260d1c30b0a6ed94cb81` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/rin-stamped.jpg` | `c58d27ab398504c8288222b2e1ead5f8fd6bb05e7f9855713a9c4ac34f7716c3` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/yui-stamped.jpg` | `a6d85fd5f64863eb72f8e1817c72b6e5c6500a0a45848cad71310e28bcab27c0` | Reika | 2026-11-05 | PASS |
