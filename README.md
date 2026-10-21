# BioAR: Organ AR Atlas

A phone AR app for the human body and 7 of its organs: brain, heart, lungs, liver, kidneys, stomach and intestines. Scan one QR code to see a glowing whole-body figure, tap an organ to open it, and place it life-size in your room. Then slice it open, pull it apart, tap any part to learn about it, and watch it work: a beating heart, breathing lungs, flowing blood and more. It runs in the phone's browser, so there's nothing to install.

## What you can do

| Tool | What it does |
| --- | --- |
| **Whole body** | The start screen: a hologram body with its skeleton and the 7 organs glowing in place (the heart beats, the lungs breathe). Tap an organ to fly into it. In AR, choose **Tabletop** or **Life-size**. **Body** brings you back. |
| **Tap a part** | Shows its name, what it does and a key fact. **Isolate** shows only that part; **Hide** removes it so you can see underneath. |
| **Slice** | Cuts the organ open from the front, side or top. Drag the slider to move the cut. Cut faces are drawn solid, in the colour of the tissue inside. |
| **Pull apart** | Separates the parts so you can see how they fit together. |
| **Parts** | A list of every part, grouped. Tap a name to select it, or the eye to hide it. |
| **How it works** | Animates what the organ does, step by step: the heart beats and pumps blue and red blood through its chambers and valves; the lungs breathe and turn blue blood red; signals travel along the brain's pathways; blood, bile and urine flow through the liver and kidneys; the stomach and intestines squeeze food along. Use the arrows or **Auto tour** to follow the steps, **See-through** to look inside, and **Sound** for the heartbeat, breath sounds and gut gurgles. Works in AR too. |
| **Health** | 3–4 common diseases per organ: what happens, warning signs, quick facts, prevention and when to see a doctor, with an emergency box where it matters. A **Healthy ↔ disease** slider shows the change on the model (a blocked coronary artery, fatty liver, kidney stones, TB nodules, stroke damage and more). **Show it working** runs the animation with the disease, for example blood held back by a blocked artery. |
| **Quiz** | 8 questions per organ: tap the named part, or pick which part a description matches. |
| **View in AR** | Places the organ life-size on your floor or table. In AR, drag with one finger to turn it, pinch to resize, tap **Move** to place it somewhere else. |

**Phones:** full AR dissection (slice, pull apart and tap parts while in AR) needs an Android phone with Chrome and Google Play Services for AR. On iPhone, **AR (basic)** opens Apple's AR viewer: the organ appears life-size, but without the slicing tools, which work in the 3D view instead. Apple doesn't let websites run custom AR.

## Parts in each organ

- **Brain (25 parts):** frontal, parietal, temporal and occipital lobes, insula and limbic cortex (left and right), white matter, basal ganglia, thalamus, hippocampus and amygdala, corpus callosum and fornix, hypothalamus and pituitary, optic chiasm, ventricles, midbrain, pons, medulla, cerebellum
- **Heart (18):** the four chambers, septum, the four valves, papillary muscles, coronary arteries and cardiac veins, aorta, pulmonary trunk, pulmonary veins, venae cavae
- **Lungs (11):** five lobes, trachea, cartilage rings, main bronchi, bronchial tree, pulmonary arteries and veins
- **Liver (14):** the eight Couinaud segments, hepatic veins, portal vein, hepatic artery, bile ducts, gallbladder, inferior vena cava
- **Kidneys (16):** capsule, cortex, columns, pyramids, papillae and sinus for each kidney, plus renal arteries and veins, aorta and vena cava
- **Stomach (8):** lower oesophagus, cardia, fundus, body, antrum, pylorus, duodenum and the folded inner lining
- **Intestines (8):** jejunum, ileum, appendix, ascending, transverse and descending colon, rectum, taeniae coli

## Put it online (free, about 10 minutes)

1. Sign in at github.com and click **New repository**. Name it `organ-ar`, set it to **Public**, and create it.
2. Click **uploading an existing file** and drag in everything in this folder, including the `models` folder. Click **Commit changes**.
3. Go to **Settings → Pages**. Under *Branch*, choose `main` and `/ (root)`, then **Save**.
4. Wait a minute or two, then refresh. Your link appears at the top, for example `https://yourname.github.io/organ-ar/`.

AR needs the page to be served over https, which GitHub Pages does for you.

## Make the QR codes

Open your link on a computer and scroll to **QR codes**. The codes already point at your link, so you can screenshot them or print the page.

Or, with Python installed:

```
pip install qrcode pillow
python3 make_qr.py https://yourname.github.io/organ-ar qr
```

The **Whole body** code (your plain link) is the main one. The others open one organ directly, using a link ending in `#heart`, `#brain`, `#lungs`, `#liver`, `#kidneys`, `#stomach` or `#intestines`.

## Change something

- **Organ facts:** edit the `ORGANS` list in `index.html`.
- **Part names and notes:** edit `models/<organ>.json`. Each part has `name`, `info` and `fact`.
- **Diseases:** edit the `HEALTH` list in `index.html`.
- **How it works steps:** edit the `FN` list in `index.html` (titles, text, which parts light up, which flows show).
- **Flow paths:** `models/<organ>.flow.json` holds the paths blood, air, food and signals follow.

## Credits and license

- **Brain, liver, stomach, intestines:** BodyParts3D, © The Database Center for Life Science (DBCLS), CC BY 4.0 (earlier releases CC BY-SA 2.1 Japan). https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html
- **Heart, lungs, kidneys and their vessels:** Human Reference Atlas 3D Reference Object Library (HuBMAP; Visible Human Male data, U.S. National Library of Medicine), CC BY 4.0. https://humanatlas.io
- **Changes made:** structures grouped into study parts and rebuilt as closed, smooth surfaces; hollow organs given real wall thickness; stomach regions and lining derived from the stomach's shape; realistic surface colour and a wet finish added; compressed for phones. Scale is preserved. The adapted models are shared under the same terms.
- **Viewer:** three.js (MIT). Sounds are synthesised in the browser (Web Audio), not recordings.
- The animations are simplified teaching models. Speeds are adjusted so you can see them.

Health information follows WHO and Indian public-health sources and is general information for learning, not medical advice. Emergency numbers shown are India's (112 and 108).

Keep the credits section in the app if you share it. The models are reference anatomy of one adult male. This app is for learning, not diagnosis.
