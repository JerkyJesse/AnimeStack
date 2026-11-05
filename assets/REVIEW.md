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

At v2.0.0 the art set was re-rendered clean: the private-stamped HUD and money copy were
removed with the two burned-in renders, the remaining character art was cropped clean, and
every card carries only public house text. The chair opened the set and signs the pass.

## The table

One row per picture under `art/` and `assets/`, excluding directory READMEs.

| File | sha256 | Reviewer | Date | Verdict |
| --- | --- | --- | --- | --- |
| `art/dossiers/aria.jpg` | `4be2f1fccc8891c28579a6861a8701e7343dcd9db734d0e4ae270bd9a1e9e5c6` | Reika | 2026-11-05 | PASS |
| `art/dossiers/elo.jpg` | `113b4d47184b3bf63fcf44e460da5b197f7c2a4d1d566248ccfa3d0a0be9db95` | Reika | 2026-11-05 | PASS |
| `art/dossiers/mechapip.jpg` | `f1fea84c234591d053dbfe69369ba9363b98db6f521cdcdfc8ffd1fa85909d2a` | Reika | 2026-11-05 | PASS |
| `art/dossiers/mei.jpg` | `945acfc1b8e3f809acfb48a3ceb2d104460c3e465d5731a323045bbbe8d844e4` | Reika | 2026-11-05 | PASS |
| `art/dossiers/niko.jpg` | `80882b618fe7c40d5889e5eaf379a244d32aa3e59c871c08e9c0efae71e350fc` | Reika | 2026-11-05 | PASS |
| `art/dossiers/reika.jpg` | `5c409995a1ea3fb2aecc15cbd33894264a51f4b2ae2dac4dfb837b8dc6e1551b` | Reika | 2026-11-05 | PASS |
| `art/dossiers/rin.jpg` | `cce0ec6a017b781d74018703b267437575729a5060bb0ab3fa935f1740b0afe5` | Reika | 2026-11-05 | PASS |
| `art/dossiers/yui.jpg` | `6b01958e14ec33324d485ca87600db20be130fedabf484526dda9f0a3523cb92` | Reika | 2026-11-05 | PASS |
| `art/sheets/aria-sheet-1.jpg` | `fac3e10903f0ea5fd991f8003ff29746ad6a13d8837663824933caaffca85d1a` | Reika | 2026-11-05 | PASS |
| `art/sheets/elo-sheet-1.jpg` | `3d1a163043191476143b50d93ef238541ccf6f9eae74e0ee81d30c9d9e9a7142` | Reika | 2026-11-05 | PASS |
| `art/sheets/mechapip-sheet-1.jpg` | `04e4272f05c2fd28c5c46bfc3d5dfa7e34c4f231206851439643c0d93a99818a` | Reika | 2026-11-05 | PASS |
| `art/sheets/mei-sheet-1.jpg` | `68fecf17291deeba262eb3fe4b4da5a71c8c6d70a27cb8c6121da33f9d5aea4d` | Reika | 2026-11-05 | PASS |
| `art/sheets/niko-sheet-1.jpg` | `065c6e19a47080956ec69d595226e66d61a838a434d8a22cebe47fa0b5c04812` | Reika | 2026-11-05 | PASS |
| `art/sheets/reika-sheet-1.jpg` | `d744c1dc4a82bce43471e26f5104cb5fbac554d425ac36bbb1b52cf92420a9f3` | Reika | 2026-11-05 | PASS |
| `art/sheets/rin-sheet-1.jpg` | `eccb2a9a979727aa2bdc75aa052bd05b317a1a1d245a30fe6777aa4396c7f3a0` | Reika | 2026-11-05 | PASS |
| `art/sheets/yui-sheet-1.jpg` | `59a8447e1064845db505abbf2bb086182c1c4e6968e12f4707c4613ff85cdd7c` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/aria-stamped.jpg` | `5341b52f8e4cad5d0bb16412a4d7712f843f6044376b6d057be5904d43eaf780` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/elo-stamped.jpg` | `4d12a94f977facb9cb17f89136a5932caddf1ecc53bb0e244eb2565bf9f52fed` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/mechapip-stamped.jpg` | `2657cd0abeb27ae1f8eede6ea3fadb93a0d02ae3d2b4a0dd4f2928965e9fb7b8` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/mei-stamped.jpg` | `d65521340f99387c965c7b836a00c40cd2889cb5477518dc1757fe13bc5b3b08` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/niko-stamped.jpg` | `3753f4405567f16154d100357b27637764c88873bb2370b6562dc6f0854acec0` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/reika-stamped.jpg` | `d4ae2d8a7a9f54247d4c7b47504fa677215864f391fa125aa5ffdad00a5ce5f9` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/rin-stamped.jpg` | `58f1e84e3f53950a862dae1e48dcedabc0561247c51df1eba3e08ffe6b0a8a01` | Reika | 2026-11-05 | PASS |
| `art/wallpapers/yui-stamped.jpg` | `2952dbfc6ceaecb8ceb99657c25a99d942f609b9c4e45a4d8985b7573a4d7ef2` | Reika | 2026-11-05 | PASS |
| `assets/img/aria-portrait.jpg` | `bb8bb210bfff6dd89b7e59374167b91fe8b301c2a5ac6e19b5344592cd3b0507` | Reika | 2026-11-05 | PASS |
| `assets/img/aria-roster.jpg` | `ad8871f40aa118471e5e815f745e0abca886dbaf1b336b964382931628d899c3` | Reika | 2026-11-05 | PASS |
| `assets/img/elo-portrait.jpg` | `b4018ea0a3f6caa3bb846007611d41a58546e70b984d8353cd8183a65f98b26e` | Reika | 2026-11-05 | PASS |
| `assets/img/elo-roster.jpg` | `9706ff92a2a36d1ca3003aceb6718eb2018e9b7e521a83d0888ce17ca9a6f3e6` | Reika | 2026-11-05 | PASS |
| `assets/img/mechapip-portrait.jpg` | `cb1fbac462f588c74aa087b91998a4af62ad407b1a85047cf2cfa540d1622063` | Reika | 2026-11-05 | PASS |
| `assets/img/mechapip-roster.jpg` | `912afebde0f328ca0699fff469124a95b91c0ff0686d5f484143a191629b7e0e` | Reika | 2026-11-05 | PASS |
| `assets/img/mei-portrait.jpg` | `7467a866d5b33ea57ba442527aaf0cfdf959665e695d2acc767ceb461057168f` | Reika | 2026-11-05 | PASS |
| `assets/img/mei-roster.jpg` | `8c0f4d4235d1751fa65637dc57becea927e3de77fb8d85bc7d80d7b7c383daee` | Reika | 2026-11-05 | PASS |
| `assets/img/niko-portrait.jpg` | `515bcff3354b493e819f242371785105f3e9f07d1ca1c4b61ff62682fc9f4bd3` | Reika | 2026-11-05 | PASS |
| `assets/img/niko-roster.jpg` | `ef22918f3682fdfee07ef2442f9390f8d15c1f6109f566e885ae64cc8967518d` | Reika | 2026-11-05 | PASS |
| `assets/img/reika-portrait.jpg` | `a833e1b296e89cf31f8d79230aef4e4d25e3c2ea4efd46d6155e95367c398a89` | Reika | 2026-11-05 | PASS |
| `assets/img/reika-roster.jpg` | `3bad6a61dc3415d83b65b9ff5240299c9eb05e27d6827cbe0316336a2aa30924` | Reika | 2026-11-05 | PASS |
| `assets/img/rin-portrait.jpg` | `934c5b5fc47c29212f2d84e7bc3e592928cfdc2c796821196651fe6320bdac8f` | Reika | 2026-11-05 | PASS |
| `assets/img/rin-roster.jpg` | `08296602b83ba9b979c0c533cea4018b03c17d1e8cbe01f2269962121aab3b0a` | Reika | 2026-11-05 | PASS |
| `assets/img/social-preview.jpg` | `6a9b77f86c8f340314e1a86a628045c7a635d9d018bcc6a183569362e150e7b6` | Reika | 2026-11-05 | PASS |
| `assets/img/team-composite.jpg` | `523333e5c46b839dec1c1772708d7a0f5183a5a617a04c96b50dae17bf5137b5` | Reika | 2026-11-05 | PASS |
| `assets/img/yui-portrait.jpg` | `31188058d4254ba1c4afa83e972364fc54d81c53c7d126e39476196583a62d07` | Reika | 2026-11-05 | PASS |
| `assets/img/yui-roster.jpg` | `6cda41efefd8c70592565c54736d071aa64d9913aab126fb717aa6721932dc4a` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/aria.jpg` | `9a5c60b7a946d82422e2f7527de374ae6f39fbabd97dcdce24998354316e687d` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/elo.jpg` | `554643dab13e43e56ec7e3019ce2d7ade4e2b81e9389b67d80324d1e84828125` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/mechapip.jpg` | `5356e53e5863ec81e153f96237ec1341b113040b9ac6a5074e1ce3bc175c3055` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/mei.jpg` | `4733a2efe99b6e18f66a9fdff3d2b0946b9115645c5f330145b956a50ac1670c` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/niko.jpg` | `c692303a35d6be5ec759444aad0068e542e251b28a2598d7098c61884dd62ed4` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/reika.jpg` | `8176e19899c04f3420e87952e395e425266644e0efb391c9abaf34082baacebe` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/rin.jpg` | `229b5154cfae0a0841e28a6add9e43b0e9801d76da540a962299e0410490d0f0` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/dossiers/yui.jpg` | `0fa8c1b74c00ca8dfbeb806a130172afe96242f71c467d34ad8f67ef898c02b3` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/aria.jpg` | `b2b649b63a1728aedb50a90614ba532fe915ec22bb04636ffed05032af35c02e` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/elo.jpg` | `969b700c0fa3fc80f0717db7c75268bd7206690528718486e3c26cfb65d98abd` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/mechapip.jpg` | `592e4a149cee33b2114a59567a380d253fe4fd53c8c0b8e75401361b94a67687` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/mei.jpg` | `3b7a7820b753e42d96144595a6e1dee2f6cc91947acc5e4e628eda131d0706a2` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/niko.jpg` | `fda9dc29277f7701801fe39caeb1c093e1b96f01d7cb967ac82936b09073e8ed` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/reika.jpg` | `d46cca5a6fd963e095c3bcf46a4d5430b909b3532e0fc617eb28630d7aed4147` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/rin.jpg` | `2e58eb8f6d960167b8cb8e22cf9f8e256d638309170076c63afd20fabde39479` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/portraits/yui.jpg` | `d11ab635f00b4a0127053a08cc267a2c298a1bf08003b9b8e3e84e7904db63ab` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/aria-sheet-1.jpg` | `f75f24238c4bee0168529b2658f13661257c0aa6ef43abc4b6211ee94c2b5a62` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/elo-sheet-1.jpg` | `26cfaece8f264ba34689b84c25e4542a370d4d0a36b06d281b7c9573509e2097` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/mechapip-sheet-1.jpg` | `481b480ed655bc874cfb0818418423b2866db45ae1c355f6dcae3173b0abea93` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/mei-sheet-1.jpg` | `f7762e8bb1d75315eecd6ce7ece526ad7b24d18a26b9554cc455194f1aaf2801` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/niko-sheet-1.jpg` | `43a633bd26ea0c07915baf8db9d924b0931f1b9f2b278246712ebb17a187ddbb` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/reika-sheet-1.jpg` | `8f5281884d7e978d47449c26d09d1a1d7fb9ca90c436cd4ca63b147aeef8fa65` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/rin-sheet-1.jpg` | `4963fb0ec4fc411e3cf845526237829f99bff5d492767e468cd8b8c4482a85d8` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/sheets/yui-sheet-1.jpg` | `d2e2f53aef0ff1aa6f6270b7b4d34ffb43c5894f7f322f7eeedcb0d72d4b21fc` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/aria-stamped.jpg` | `949faa48a2d378f0bc534aa01a4407556989ccea9ed89d03d476f5af1fd7baa9` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/elo-stamped.jpg` | `d94bad833e8f028b0c4f1ace9bcca6a85eb6bc0384837690377b1d573b66759a` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/mechapip-stamped.jpg` | `768bbe5ffef659891578b227b6fd7e1407c0aa42703f3bef888c5d5ed13295de` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/mei-stamped.jpg` | `3bad584b3c224e8335eadf77c00319cf199f0ffecaff294350a24df07295e936` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/niko-stamped.jpg` | `5ceebcabd411f68696c9bf5b6c89c7a501d16d46dcc9e29927fb84022ce763d6` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/reika-stamped.jpg` | `26e978eaa3c7c51b8149835d76efe465fd9f7bfe73214aeece9d22aa1b589939` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/rin-stamped.jpg` | `3d312af3341ec8ada65ecf95c5c1eec1a5f5f596d4208cd1ef41238534799543` | Reika | 2026-11-05 | PASS |
| `assets/thumbs/wallpapers/yui-stamped.jpg` | `10aa1f3b879865b351c475481af3201eac4b67f566f18bc921e7c20190fbf9b2` | Reika | 2026-11-05 | PASS |
