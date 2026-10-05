# Future site motion

Proposed adaptations of the founder-approved [[Motion Style Guide]], recorded October 4, 2026. Initial ideas are listed below, with implementation status tracked in the update section.

## First additions

| Priority | Placement | Proposed experience | Implementation direction |
| --- | --- | --- | --- |
| 1 | Homepage product introduction | “Build something real” enters once in a short sequence; a static final headline remains alongside the existing calls to action | Real DOM text with masked/translated word spans, opacity and colour accents; trigger once when visible |
| 2 | Hosting / dashboard introduction | A concise workspace demonstration shows hosting, APIs and scripts; a cursor click carries the viewer into a terminal preview | A separate demo panel with HTML/CSS cards, a decorative cursor and staged states; label sample states clearly |
| 3 | Registry group introduction | One morphing grid suggests the different capability families, then settles behind or beside readable group headings | SVG path interpolation or a single Canvas 2D surface, using the reel's contour families |
| 4 | Shared page / section transition | A brief branded stripe reveal exposes the destination without holding navigation for a long animation | CSS masks or transformed shutter elements; start loading immediately and remove the overlay promptly |
| 5 | A single homepage or Registry signature | Replace a selected existing dot sculpture with a depth-aware particle sphere rather than stacking a new loop on top | Project 3D point coordinates into a 2D canvas; pause when hidden or offscreen |

Suggested first prototype: pair the homepage word entrance with a small hosting walkthrough. That tests the accepted style directly against the site's goal of helping people understand and build useful projects.

## Richer experiments after that

| Effect | Suitable location | Treatment |
| --- | --- | --- |
| Glossy pink forms | One homepage feature or hosting hero | Start with a short silent WebM/MP4 and still poster; consider WebGL only if interaction adds value and measured performance permits it |
| Halftone reveal | A feature introduction, editorial section or brief navigation accent | A masked decorative layer; preserve readable headings and allow a static composition |
| SVG logo reveal | Initial brand introduction or the end of a product walkthrough | Animate the existing wordmark mask once, then retain a crisp still mark |
| HUD framing | A dedicated product walkthrough or video player | Keep it within the demo presentation; labels can describe the scene rather than implying live monitoring |
| Cursor interactions | A tutorial that demonstrates a specific control | Confine the animated pointer to the demonstration; ordinary page controls continue to use the visitor's own pointer and focus state |

The reel's beat grid can guide promotional media embedded on the site. The site itself should work silently, with user-triggered playback for the soundtrack.

## Web motion settings to prototype

These are starting values to tune in browser, not values already implemented:

| Motion | Initial target |
| --- | --- |
| Small hover or focus feedback | 120–180ms |
| Word or card entrance | 300–500ms, 60–100ms stagger |
| Stripe navigation accent | 180–300ms; avoid extending existing navigation delays |
| Demonstration step | 700–1,200ms, with enough time to read the changed state |
| Particle / morph ambient cycle | 8–16 seconds, with subtle amplitude |
| Spring entrance | One modest overshoot, then settle |

Use the reel's ease-out profile, `1 - (1 - t)^4`, for confident entrances. Its spring profile, `1 - exp(-8t) * cos(11t)`, is a useful reference for isolated card motion; tune overshoot down for real controls. Final website text should remain real selectable DOM content.

## Fit with the current code

- `styles.css`: add scoped motion classes and tokens for entrances, stripes and masks; preserve existing palette and custom identity.
- `app.js`: extend or consolidate the shared dot renderer and visibility handling for the sphere/grid. Inspect existing independent loops before adding another clock.
- `navigateWithTransition`: review the existing 840ms navigation wait when prototyping the shorter stripe reveal.
- `index.html`: place kinetic copy and a single visual signature within the product introduction, leaving the main navigation and calls to action clear.
- `hosting.html` / `hosting.js`: use a walkthrough to explain the workspace plan and intended hosting flow. The current site does not provision purchased servers or provide a live terminal.
- `registry.html`: keep individual capability cards stable while one group-level graphic carries the motion.
- `dashboard.html`: show real saved-plan or project state where available; animations can explain a change without inventing a successful deployment.

## Acceptance checks for an implementation

A site adaptation should have a readable static state, honor `prefers-reduced-motion`, pause expensive work when hidden/offscreen, and avoid capturing input or obscuring focus. On touch devices, it should fit the layout without pointer-dependent behavior. Size particle counts, pixel density and shader work against measured device performance; the reel's 60fps output is not a universal site requirement.

Check the visible effect alongside the actual workflow on desktop and mobile: legibility, navigation responsiveness, control activation and absence of layout shifts. If using a shader or video, provide a poster or still fallback so the product message remains available.

See [[Roadmap]], [[Dot Motion Update]], [[Experience Direction]] and [[Motion Style Guide]].

## First implementation — October 4, 2026

See [[Approved Site Motion]] for screenshots and validation. Implemented the homepage kinetic headline and logo entrance, hosting walkthrough, Registry sphere, shared stripe transitions and one glossy pink homepage visual. The video pauses offscreen and has a manual control. Reduced-motion and no-JavaScript states were verified.

A morphing Registry grid, broader halftone section reveals and interactive WebGL artwork remain possible future experiments.

## Latest site revision

See [[Project Workspace Redesign]]. The homepage glossy loop has been replaced by an interactive project starter, and stripe navigation has been slowed. Earlier descriptions of those two effects describe the prior implementation. The approved promo reel remains unchanged.

## October 5 implementation

The new website uses dot horizons, arched fields, signal waves, and ripples. Striped navigation, rotating Registry sculpture, and the demonstration cursor were retired. See [[Creative Refresh]]. The approved video remains a separate creative reference.

## Latest dark workspace implementation

[[Dark Creative Rebuild]] adds breathing bloom and crossing weave patterns, a shared 30fps dot clock, pause/resume, and once-only section entrances. This is the current workspace direction.
