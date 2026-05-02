from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
FLOWER_DIR = APP_DIR / "flower-blooming"


def _flower_body() -> str:
    html = (FLOWER_DIR / "index.html").read_text(encoding="utf-8")
    start = html.index("<body")
    start = html.index(">", start) + 1
    end = html.rindex("</body>")
    return html[start:end]


def _extra_flowers() -> str:
    return """
      <div class="flower flower--4 color-rose">
        <div class="flower__leafs flower__leafs--4">
          <div class="flower__leaf flower__leaf--1"></div>
          <div class="flower__leaf flower__leaf--2"></div>
          <div class="flower__leaf flower__leaf--3"></div>
          <div class="flower__leaf flower__leaf--4"></div>
          <div class="flower__white-circle"></div>
          <div class="flower__light flower__light--1"></div>
          <div class="flower__light flower__light--2"></div>
          <div class="flower__light flower__light--3"></div>
          <div class="flower__light flower__light--4"></div>
          <div class="flower__light flower__light--5"></div>
          <div class="flower__light flower__light--6"></div>
          <div class="flower__light flower__light--7"></div>
          <div class="flower__light flower__light--8"></div>
        </div>
        <div class="flower__line">
          <div class="flower__line__leaf flower__line__leaf--1"></div>
          <div class="flower__line__leaf flower__line__leaf--2"></div>
          <div class="flower__line__leaf flower__line__leaf--3"></div>
          <div class="flower__line__leaf flower__line__leaf--4"></div>
        </div>
      </div>

      <div class="flower flower--5 color-gold">
        <div class="flower__leafs flower__leafs--5 tulip-head">
          <div class="flower__leaf flower__leaf--1"></div>
          <div class="flower__leaf flower__leaf--2"></div>
          <div class="flower__leaf flower__leaf--3"></div>
          <div class="flower__leaf flower__leaf--4"></div>
          <div class="flower__white-circle"></div>
          <div class="flower__light flower__light--1"></div>
          <div class="flower__light flower__light--2"></div>
          <div class="flower__light flower__light--3"></div>
          <div class="flower__light flower__light--4"></div>
          <div class="flower__light flower__light--5"></div>
          <div class="flower__light flower__light--6"></div>
          <div class="flower__light flower__light--7"></div>
          <div class="flower__light flower__light--8"></div>
        </div>
        <div class="flower__line">
          <div class="flower__line__leaf flower__line__leaf--1"></div>
          <div class="flower__line__leaf flower__line__leaf--2"></div>
          <div class="flower__line__leaf flower__line__leaf--3"></div>
          <div class="flower__line__leaf flower__line__leaf--4"></div>
        </div>
      </div>

      <div class="flower flower--6 color-lilac">
        <div class="flower__leafs flower__leafs--6">
          <div class="flower__leaf flower__leaf--1"></div>
          <div class="flower__leaf flower__leaf--2"></div>
          <div class="flower__leaf flower__leaf--3"></div>
          <div class="flower__leaf flower__leaf--4"></div>
          <div class="flower__white-circle"></div>
          <div class="flower__light flower__light--1"></div>
          <div class="flower__light flower__light--2"></div>
          <div class="flower__light flower__light--3"></div>
          <div class="flower__light flower__light--4"></div>
          <div class="flower__light flower__light--5"></div>
          <div class="flower__light flower__light--6"></div>
          <div class="flower__light flower__light--7"></div>
          <div class="flower__light flower__light--8"></div>
        </div>
        <div class="flower__line">
          <div class="flower__line__leaf flower__line__leaf--1"></div>
          <div class="flower__line__leaf flower__line__leaf--2"></div>
          <div class="flower__line__leaf flower__line__leaf--3"></div>
          <div class="flower__line__leaf flower__line__leaf--4"></div>
          <div class="flower__line__leaf flower__line__leaf--5"></div>
          <div class="flower__line__leaf flower__line__leaf--6"></div>
        </div>
      </div>

      <div class="flower flower--7 color-coral">
        <div class="flower__leafs flower__leafs--7 tulip-head">
          <div class="flower__leaf flower__leaf--1"></div>
          <div class="flower__leaf flower__leaf--2"></div>
          <div class="flower__leaf flower__leaf--3"></div>
          <div class="flower__leaf flower__leaf--4"></div>
          <div class="flower__white-circle"></div>
          <div class="flower__light flower__light--1"></div>
          <div class="flower__light flower__light--2"></div>
          <div class="flower__light flower__light--3"></div>
          <div class="flower__light flower__light--4"></div>
          <div class="flower__light flower__light--5"></div>
          <div class="flower__light flower__light--6"></div>
          <div class="flower__light flower__light--7"></div>
          <div class="flower__light flower__light--8"></div>
        </div>
        <div class="flower__line">
          <div class="flower__line__leaf flower__line__leaf--1"></div>
          <div class="flower__line__leaf flower__line__leaf--2"></div>
          <div class="flower__line__leaf flower__line__leaf--3"></div>
          <div class="flower__line__leaf flower__line__leaf--4"></div>
        </div>
      </div>
"""


def _component_html() -> str:
    flower_css = (FLOWER_DIR / "style.css").read_text(encoding="utf-8")
    flower_markup = _flower_body().replace(
        '      <div class="grow-ans" style="--d:1.2s">',
        f"{_extra_flowers()}\n      <div class=\"grow-ans\" style=\"--d:1.2s\">",
        1,
    )

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    {flower_css}

    :root {{
      --bloom: 0.72;
      --head-scale: 0.82;
      --leaf-scale: 0.72;
      --glow: 0.72;
      --hold-x: 50%;
      --hold-y: 76%;
      --bouquet-scale: 0.86;
      --bouquet-opacity: 0;
    }}

    html,
    body {{
      width: 100%;
      height: 100%;
    }}

    body {{
      min-height: 820px;
      padding: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      align-items: stretch;
      justify-content: stretch;
      background:
        radial-gradient(circle at var(--hold-x) var(--hold-y), rgba(48, 255, 228, calc(0.28 * var(--glow))), transparent 26%),
        radial-gradient(circle at 22% 18%, rgba(255, 232, 120, 0.08), transparent 18%),
        #000;
    }}

    .night {{
      display: none;
    }}

    .flowers {{
      position: fixed;
      left: var(--hold-x);
      top: var(--hold-y);
      transform: translate(-50%, -64%) scale(var(--bouquet-scale));
      z-index: 60;
      pointer-events: none;
      opacity: var(--bouquet-opacity);
      transition: transform 220ms ease-out, filter 220ms ease-out;
      filter:
        saturate(calc(1 + (var(--glow) * 0.42)))
        drop-shadow(0 0 calc(1vmin + (var(--glow) * 2.8vmin)) rgba(107, 240, 255, 0.48));
    }}

    .flower__line {{
      transform-origin: bottom center;
    }}

    .flower__leafs {{
      transform: scale(var(--head-scale));
      transform-origin: bottom center;
      transition: transform 180ms ease-out, opacity 180ms ease-out;
      opacity: calc(0.72 + (var(--bloom) * 0.28));
    }}

    .flower__line__leaf,
    .grow-ans,
    .growing-grass {{
      scale: var(--leaf-scale);
      transform-origin: bottom center;
      transition: scale 180ms ease-out, opacity 180ms ease-out;
      opacity: calc(0.55 + (var(--bloom) * 0.45));
    }}

    .flower__leaf {{
      background-color: var(--petal-light, #a7ffee);
      background-image: linear-gradient(to top, var(--petal-dark, #54b8aa), var(--petal-light, #a7ffee));
    }}

    .flower__leaf--4 {{
      background-image: linear-gradient(to top, var(--petal-accent, #39c6d6), var(--petal-light, #a7ffee));
    }}

    .flower__leafs::after {{
      background-color: var(--petal-glow, #6bf0ff);
      opacity: calc(0.45 + (var(--glow) * 0.5));
    }}

    .flower__light {{
      opacity: calc(0.35 + (var(--glow) * 0.65));
      box-shadow: 0 0 calc(0.4vmin + (var(--glow) * 1.4vmin)) var(--petal-glow, #6bf0ff);
    }}

    .color-rose {{
      --petal-light: #ffd1df;
      --petal-dark: #e74679;
      --petal-accent: #ff7aa7;
      --petal-glow: #ff8eb8;
    }}

    .color-gold {{
      --petal-light: #fff0a6;
      --petal-dark: #f0a91f;
      --petal-accent: #ffcf4d;
      --petal-glow: #ffe47a;
    }}

    .color-lilac {{
      --petal-light: #decaff;
      --petal-dark: #7a55d6;
      --petal-accent: #a78bfa;
      --petal-glow: #c4b5fd;
    }}

    .color-coral {{
      --petal-light: #ffc8b8;
      --petal-dark: #f05c4f;
      --petal-accent: #ff8f76;
      --petal-glow: #ffae99;
    }}

    .flower--4 {{
      left: -38%;
      transform: rotate(-26deg) scale(0.9);
      animation: moving-flower-3 4.6s linear infinite;
    }}

    .flower--4 .flower__line {{
      height: 52vmin;
    }}

    .flower--5 {{
      left: 26%;
      transform: rotate(8deg) scale(0.86);
      animation: moving-flower-1 4.2s linear infinite;
    }}

    .flower--5 .flower__line {{
      height: 64vmin;
    }}

    .flower--6 {{
      left: -8%;
      transform: rotate(-7deg) scale(0.82);
      animation: moving-flower-2 5s linear infinite;
      z-index: 8;
    }}

    .flower--6 .flower__line {{
      height: 58vmin;
    }}

    .flower--7 {{
      left: 72%;
      transform: rotate(28deg) scale(0.74);
      animation: moving-flower-2 4.8s linear infinite;
      z-index: 7;
    }}

    .flower--7 .flower__line {{
      height: 48vmin;
    }}

    .flower--4 .flower__line__leaf,
    .flower--5 .flower__line__leaf,
    .flower--6 .flower__line__leaf,
    .flower--7 .flower__line__leaf {{
      animation: blooming-leaf-right var(--fl-speed) 1.2s backwards;
    }}

    .tulip-head .flower__leaf {{
      border-radius: 54% 46% 38% 62% / 35% 34% 66% 65%;
    }}

    .tulip-head .flower__leaf--2 {{
      height: 12.5vmin;
      transform: translate(-50%, -6%) rotateX(18deg) scaleX(0.92);
    }}

    .tulip-head .flower__white-circle {{
      width: 6.5vmin;
      height: 2.8vmin;
      left: -2.4vmin;
      top: -1.8vmin;
      opacity: 0.72;
    }}

    .gesture-panel {{
      position: fixed;
      inset: 0;
      z-index: 20;
      width: 100%;
      height: 100%;
      color: rgba(241, 255, 252, 0.92);
      pointer-events: none;
    }}

    .camera-shell {{
      position: absolute;
      inset: 0;
      overflow: hidden;
      border: 0;
      border-radius: 0;
      background: rgba(2, 10, 14, 0.72);
      box-shadow: none;
    }}

    video,
    canvas {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    video {{
      opacity: 0.86;
      filter: contrast(1.06) saturate(0.9) brightness(0.72);
      transform: scaleX(-1);
    }}

    canvas {{
      z-index: 80;
      transform: none;
    }}

    .hud {{
      position: absolute;
      left: 18px;
      bottom: 18px;
      z-index: 120;
      width: min(360px, calc(100vw - 36px));
      padding: 10px 12px;
      border: 1px solid rgba(151, 255, 240, 0.18);
      border-radius: 8px;
      background: rgba(1, 9, 12, 0.7);
      backdrop-filter: blur(10px);
    }}

    .instructions {{
      position: absolute;
      right: 18px;
      top: 18px;
      z-index: 120;
      width: min(340px, calc(100vw - 36px));
      padding: 12px 14px;
      border: 1px solid rgba(151, 255, 240, 0.18);
      border-radius: 8px;
      background: rgba(1, 9, 12, 0.68);
      backdrop-filter: blur(10px);
      font-size: 13px;
      line-height: 1.45;
      color: rgba(241, 255, 252, 0.9);
    }}

    .instructions strong {{
      display: block;
      margin-bottom: 4px;
      color: #fff1a8;
      font-weight: 700;
    }}

    .instructions span {{
      display: block;
      color: rgba(220, 255, 249, 0.78);
    }}

    .hud-row {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      font-size: 13px;
      line-height: 1.35;
    }}

    .status {{
      color: rgba(241, 255, 252, 0.9);
      white-space: nowrap;
    }}

    .error-note {{
      display: none;
      margin-top: 8px;
      font-size: 12px;
      line-height: 1.35;
      color: rgba(255, 220, 186, 0.88);
    }}

    .error-note.is-visible {{
      display: block;
    }}

    .meter {{
      position: relative;
      height: 7px;
      margin-top: 9px;
      overflow: hidden;
      border-radius: 999px;
      background: rgba(151, 255, 240, 0.13);
    }}

    .meter > span {{
      position: absolute;
      inset: 0 auto 0 0;
      width: calc(var(--bloom) * 100%);
      border-radius: inherit;
      background: linear-gradient(90deg, #39c6d6, #fff1a8);
      box-shadow: 0 0 18px rgba(107, 240, 255, 0.52);
      transition: width 180ms ease-out;
    }}

    .fallback {{
      display: none;
      margin-top: 8px;
      gap: 8px;
      align-items: center;
      font-size: 12px;
      color: rgba(220, 255, 249, 0.78);
    }}

    .fallback.is-visible {{
      display: flex;
    }}

    input[type="range"] {{
      width: 100%;
      accent-color: #6bf0ff;
    }}

    @media (max-width: 760px) {{
      body {{
        min-height: 820px;
      }}

      .hud {{
        left: 12px;
        bottom: 12px;
        width: min(310px, calc(100vw - 24px));
      }}

      .instructions {{
        left: 12px;
        right: auto;
        top: 12px;
        width: min(330px, calc(100vw - 24px));
      }}

      .hud-row {{
        font-size: 12px;
      }}
    }}
  </style>
</head>
<body>
  <section class="gesture-panel" aria-label="Hand controlled bloom">
    <div class="camera-shell">
      <video id="camera" autoplay playsinline muted></video>
      <canvas id="overlay"></canvas>
    </div>
    <div class="instructions">
      <strong>Grip hand: closed fist to hold bouquet</strong>
      <span>Tuck all four fingertips toward the knuckles. The bouquet appears only when this grip is detected.</span>
      <span>Other hand: pinch open or close to bloom.</span>
    </div>
    <div class="hud">
      <div class="hud-row">
        <span id="hint">Allow camera, then pinch open</span>
        <span class="status" id="status">starting</span>
      </div>
      <div class="meter" aria-hidden="true"><span></span></div>
      <label class="fallback" id="fallback">
        manual bloom
        <input id="manualBloom" type="range" min="0" max="100" value="72" />
      </label>
      <div class="error-note" id="errorNote"></div>
    </div>
  </section>

  {flower_markup}

  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js"></script>
  <script>
    const root = document.documentElement;
    const video = document.getElementById("camera");
    const canvas = document.getElementById("overlay");
    const ctx = canvas.getContext("2d");
    const statusText = document.getElementById("status");
    const hintText = document.getElementById("hint");
    const fallback = document.getElementById("fallback");
    const errorNote = document.getElementById("errorNote");
    const manualBloom = document.getElementById("manualBloom");

    let bloom = 0.72;
    let targetBloom = 0.72;
    let holdX = 50;
    let holdY = 76;
    let targetHoldX = 50;
    let targetHoldY = 76;
    let bouquetOpacity = 0;
    let targetBouquetOpacity = 0;
    let lastHandAt = 0;

    const clamp = (value, min, max) => Math.min(max, Math.max(min, value));
    const mapRange = (value, inMin, inMax, outMin, outMax) => {{
      const amount = clamp((value - inMin) / (inMax - inMin), 0, 1);
      return outMin + amount * (outMax - outMin);
    }};

    function setBloom(value) {{
      targetBloom = clamp(value, 0.28, 1);
    }}

    function showManual(message) {{
      fallback.classList.add("is-visible");
      errorNote.textContent = message;
      errorNote.classList.add("is-visible");
      statusText.textContent = "manual";
    }}

    function renderBloom() {{
      bloom += (targetBloom - bloom) * 0.18;
      holdX += (targetHoldX - holdX) * 0.16;
      holdY += (targetHoldY - holdY) * 0.16;
      bouquetOpacity += (targetBouquetOpacity - bouquetOpacity) * 0.2;
      const headScale = mapRange(bloom, 0.28, 1, 0.58, 1.08);
      const leafScale = mapRange(bloom, 0.28, 1, 0.72, 1.06);
      const bouquetScale = mapRange(bloom, 0.28, 1, 0.78, 0.92);
      const glow = mapRange(bloom, 0.28, 1, 0.35, 1.45);

      root.style.setProperty("--bloom", bloom.toFixed(3));
      root.style.setProperty("--head-scale", headScale.toFixed(3));
      root.style.setProperty("--leaf-scale", leafScale.toFixed(3));
      root.style.setProperty("--glow", glow.toFixed(3));
      root.style.setProperty("--hold-x", `${{holdX.toFixed(2)}}%`);
      root.style.setProperty("--hold-y", `${{holdY.toFixed(2)}}%`);
      root.style.setProperty("--bouquet-scale", bouquetScale.toFixed(3));
      root.style.setProperty("--bouquet-opacity", bouquetOpacity.toFixed(3));

      requestAnimationFrame(renderBloom);
    }}

    function resizeCanvas() {{
      const rect = canvas.getBoundingClientRect();
      canvas.width = Math.max(1, Math.floor(rect.width * window.devicePixelRatio));
      canvas.height = Math.max(1, Math.floor(rect.height * window.devicePixelRatio));
      ctx.setTransform(window.devicePixelRatio, 0, 0, window.devicePixelRatio, 0, 0);
    }}

    function pointToDisplay(point) {{
      const rect = canvas.getBoundingClientRect();
      const viewW = Math.max(1, rect.width);
      const viewH = Math.max(1, rect.height);
      const sourceW = video.videoWidth || 640;
      const sourceH = video.videoHeight || 480;
      const coverScale = Math.max(viewW / sourceW, viewH / sourceH);
      const renderedW = sourceW * coverScale;
      const renderedH = sourceH * coverScale;
      const offsetX = (viewW - renderedW) / 2;
      const offsetY = (viewH - renderedH) / 2;
      const displayX = ((point.x * renderedW) + offsetX) / viewW;
      const y = ((point.y * renderedH) + offsetY) / viewH;
      return {{
        x: clamp(displayX, 0, 1),
        y: clamp(y, 0, 1),
      }};
    }}

    function drawPoint(point, radius, fillStyle) {{
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      const display = pointToDisplay(point);
      ctx.beginPath();
      ctx.arc(display.x * width, display.y * height, radius, 0, Math.PI * 2);
      ctx.fillStyle = fillStyle;
      ctx.fill();
    }}

    function drawLine(from, to, strokeStyle, lineWidth = 2) {{
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      const displayFrom = pointToDisplay(from);
      const displayTo = pointToDisplay(to);
      ctx.beginPath();
      ctx.moveTo(displayFrom.x * width, displayFrom.y * height);
      ctx.lineTo(displayTo.x * width, displayTo.y * height);
      ctx.lineWidth = lineWidth;
      ctx.strokeStyle = strokeStyle;
      ctx.stroke();
    }}

    function handScale(landmarks) {{
      const wrist = landmarks[0];
      const middleBase = landmarks[9];
      return Math.max(0.04, Math.hypot(wrist.x - middleBase.x, wrist.y - middleBase.y));
    }}

    function pinchAmount(landmarks) {{
      const thumb = landmarks[4];
      const index = landmarks[8];
      const pinchDistance = Math.hypot(thumb.x - index.x, thumb.y - index.y);
      return pinchDistance / handScale(landmarks);
    }}

    function fistScore(landmarks) {{
      const scale = handScale(landmarks);
      const palm = landmarks[9];
      const fingers = [
        {{ mcp: 5, pip: 6, dip: 7, tip: 8 }},
        {{ mcp: 9, pip: 10, dip: 11, tip: 12 }},
        {{ mcp: 13, pip: 14, dip: 15, tip: 16 }},
        {{ mcp: 17, pip: 18, dip: 19, tip: 20 }},
      ];

      const curlScores = fingers.map((finger) => {{
        const mcp = landmarks[finger.mcp];
        const pip = landmarks[finger.pip];
        const dip = landmarks[finger.dip];
        const tip = landmarks[finger.tip];
        const knuckleSpan = Math.hypot(pip.x - mcp.x, pip.y - mcp.y) / scale;
        const tipToMcp = Math.hypot(tip.x - mcp.x, tip.y - mcp.y) / scale;
        const tipToPalm = Math.hypot(tip.x - palm.x, tip.y - palm.y) / scale;
        const tipToDip = Math.hypot(tip.x - dip.x, tip.y - dip.y) / scale;
        const tuckedToKnuckle = clamp(mapRange(tipToMcp, 1.18, 0.45, 0, 1), 0, 1);
        const tuckedToPalm = clamp(mapRange(tipToPalm, 1.7, 0.62, 0, 1), 0, 1);
        const shortTipSegment = clamp(mapRange(tipToDip, 0.72, 0.28, 0, 1), 0, 1);
        const visibleKnuckle = clamp(mapRange(knuckleSpan, 0.22, 0.58, 0, 1), 0, 1);
        return (tuckedToKnuckle * 0.42) + (tuckedToPalm * 0.28) + (shortTipSegment * 0.16) + (visibleKnuckle * 0.14);
      }});

      const averageCurl = curlScores.reduce((sum, score) => sum + score, 0) / curlScores.length;
      const curledFingerCount = curlScores.filter((score) => score > 0.5).length / curlScores.length;
      return clamp((averageCurl * 0.72) + (curledFingerCount * 0.28), 0, 1);
    }}

    function handLabel(index, landmarks, handedness) {{
      const raw = handedness?.[index];
      const label = raw?.label || raw?.[0]?.label || raw?.classification?.[0]?.label;
      if (label === "Left" || label === "Right") return label;
      return landmarks[9].x < 0.5 ? "Right" : "Left";
    }}

    function setHoldFromHand(landmarks) {{
      const palm = landmarks[9];
      const display = pointToDisplay(palm);
      targetHoldX = clamp(display.x * 100, 10, 90);
      targetHoldY = clamp((display.y * 100) + 4, 24, 90);
    }}

    function drawHands(holdHand, bloomHand) {{
      resizeCanvas();
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      ctx.clearRect(0, 0, width, height);

      if (holdHand) {{
        const palm = holdHand[9];
        const wrist = holdHand[0];
        const fingerJoints = [5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20];
        drawPoint(palm, 18, "rgba(255, 241, 168, 0.18)");
        const displayPalm = pointToDisplay(palm);
        ctx.beginPath();
        ctx.arc(displayPalm.x * width, displayPalm.y * height, 18, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(255, 241, 168, 0.95)";
        ctx.lineWidth = 2;
        ctx.stroke();
        drawLine(wrist, palm, "rgba(107, 240, 255, 0.75)", 2);
        fingerJoints.forEach((jointIndex) => {{
          const joint = holdHand[jointIndex];
          drawPoint(joint, jointIndex % 4 === 0 ? 5 : 3.5, jointIndex % 4 === 0 ? "rgba(255, 241, 168, 0.95)" : "rgba(107, 240, 255, 0.82)");
        }});
      }}

      if (!bloomHand) return;

      const thumb = bloomHand[4];
      const index = bloomHand[8];
      const points = [thumb, index];

      ctx.lineWidth = 3;
      ctx.strokeStyle = "rgba(255, 241, 168, 0.95)";
      ctx.beginPath();
      points.forEach((point, index) => {{
        const display = pointToDisplay(point);
        const x = display.x * width;
        const y = display.y * height;
        if (index === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }});
      ctx.stroke();

      points.forEach((point) => {{
        const display = pointToDisplay(point);
        ctx.beginPath();
        ctx.arc(display.x * width, display.y * height, 7, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(107, 240, 255, 0.9)";
        ctx.fill();
        ctx.strokeStyle = "rgba(255, 255, 255, 0.9)";
        ctx.stroke();
      }});
    }}

    function onResults(results) {{
      if (!results.multiHandLandmarks || results.multiHandLandmarks.length === 0) {{
        const age = performance.now() - lastHandAt;
        if (age > 700) {{
          statusText.textContent = "show hand";
          hintText.textContent = "close one hand into a grip";
          ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
          targetBouquetOpacity = 0;
          setBloom(0.28);
        }}
        return;
      }}

      const hands = results.multiHandLandmarks.map((landmarks, index) => ({{
        landmarks,
        index,
        label: handLabel(index, landmarks, results.multiHandedness),
        fist: fistScore(landmarks),
        pinch: pinchAmount(landmarks),
        palmY: landmarks[9].y,
      }}));

      const holdCandidate = hands.reduce((best, hand) => hand.fist > best.fist ? hand : best, hands[0]);
      const holdHand = holdCandidate.fist > 0.46 ? holdCandidate : null;

      if (!holdHand) {{
        targetBouquetOpacity = 0;
        setBloom(0.28);
        drawHands(null, null);
        lastHandAt = performance.now();
        statusText.textContent = "locked";
        const seen = hands.map((hand) => `${{hand.label}} ${{Math.round(hand.fist * 100)}}%`).join(", ");
        hintText.textContent = seen ? `need grip (${{seen}})` : "close one hand into a grip";
        return;
      }}

      targetBouquetOpacity = 1;
      const bloomCandidates = hands.filter((hand) => hand.index !== holdHand.index);
      const bloomHand = bloomCandidates.length > 0
        ? bloomCandidates.reduce((best, hand) => hand.pinch > best.pinch ? hand : best, bloomCandidates[0])
        : null;

      setHoldFromHand(holdHand.landmarks);
      const nextBloom = bloomHand ? mapRange(bloomHand.pinch, 0.55, 1.75, 0.28, 1) : targetBloom;

      lastHandAt = performance.now();
      setBloom(nextBloom);
      drawHands(holdHand.landmarks, bloomHand?.landmarks);

      const direction = nextBloom > bloom + 0.03 ? "opening" : nextBloom < bloom - 0.03 ? "settling" : "holding";
      statusText.textContent = `${{Math.round(nextBloom * 100)}}%`;
      if (bloomHand) {{
        hintText.textContent = direction === "opening" ? "grip + blooming" : direction === "settling" ? "grip + soft close" : "bouquet active";
      }} else {{
        hintText.textContent = hands.length < 2 ? "grip held, bring other hand in" : "hold grip, pinch with other hand";
      }}
    }}

    async function startHands() {{
      renderBloom();

      if (!navigator.mediaDevices?.getUserMedia) {{
        hintText.textContent = "camera unavailable";
        showManual("This browser context does not expose getUserMedia. Try Chrome or Edge on localhost.");
        return;
      }}

      if (!window.Hands) {{
        hintText.textContent = "tracking unavailable";
        showManual("MediaPipe Hands did not load. Check your internet connection because the model loads from CDN.");
        return;
      }}

      try {{
        statusText.textContent = "asking";
        hintText.textContent = "allow camera access";

        const stream = await navigator.mediaDevices.getUserMedia({{
          video: {{
            width: {{ ideal: 640 }},
            height: {{ ideal: 480 }},
            facingMode: "user",
          }},
          audio: false,
        }});

        video.srcObject = stream;
        await video.play();
        resizeCanvas();

        const hands = new Hands({{
          locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${{file}}`,
        }});

        hands.setOptions({{
          maxNumHands: 2,
          modelComplexity: 0,
          minDetectionConfidence: 0.42,
          minTrackingConfidence: 0.42,
          selfieMode: true,
        }});

        hands.onResults(onResults);

        let processing = false;
        const processFrame = async () => {{
          if (!video.paused && !video.ended && !processing) {{
            processing = true;
            await hands.send({{ image: video }});
            processing = false;
          }}
          requestAnimationFrame(processFrame);
        }};

        statusText.textContent = "ready";
        hintText.textContent = "pinch open to bloom";
        processFrame();
      }} catch (error) {{
        console.error(error);
        hintText.textContent = "camera did not start";
        showManual(`${{error.name || "CameraError"}}: ${{error.message || "Unable to start camera/tracking."}}`);
      }}
    }}

    manualBloom.addEventListener("input", (event) => {{
      setBloom(Number(event.target.value) / 100);
      statusText.textContent = `${{event.target.value}}%`;
    }});

    window.addEventListener("resize", resizeCanvas);
    window.addEventListener("load", startHands);
  </script>
</body>
</html>
"""


def main() -> None:
    st.set_page_config(page_title="Hand Bloom", page_icon="🌸", layout="wide")
    st.markdown(
        """
        <style>
          #MainMenu, header, footer { visibility: hidden; }
          .stApp { background: #000; }
          .block-container { padding: 0; max-width: 100%; }
          iframe { display: block; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    components.html(_component_html(), height=820, scrolling=False)


if __name__ == "__main__":
    main()
