#!/usr/bin/env python3
import os
import sys
from pathlib import Path
XARA_GALLERY = False

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.append(os.path.abspath("_setup"))

suppress_warnings = [
    "toc.not_included",
    "ref.footnote",
    "ref.citation",
    "toc.not_readable",
    "misc.highlighting_failure",
    "bibtex.key_not_found"
]

#
# Project information
#
project = "xara"
copyright = 'Berkeley, CA'
description = "Finite element analysis"
author = "PEER"
#html_logo = "_static/images/xara.png"
html_title = "xara: Nonlinear finite element analysis" # "xara: An OpenSees application"
html_short_title = "xara"

root_doc = "launch" #"user/index"
html_additional_pages = {'index': 'home.html'}
html_extra_path = ["robots.txt"]
from _setup.prolog import rst_prolog


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#   'toctree_filter',
    # "myst_parser",
    "myst_nb",
    "xara_sphinx_gallery" if XARA_GALLERY else "myst_sphinx_gallery",
    'sphinxcontrib.googleanalytics',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinx.ext.autodoc',
    "sphinx.ext.autosummary",
    "sphinxcontrib.bibtex",
    "sphinx.ext.napoleon",
    "sphinx_sitemap",
    "sphinx_design",
    # "sphinx_codeautolink",

    "param_dl",
    "version_notes",
]

codeautolink_warn_on_failed_resolve = True
codeautolink_warn_on_missing_inventory = True
codeautolink_warn_on_no_backreference = True
codeautolink_warn_on_default_parse_fail = True
codeautolink_inventory_map = {
    # "opensees.openseespy": "xara"
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-nb",
    ".myst": "myst-nb",
}

autosummary_generate = False
autodoc_docstring_signature = True

nb_execution_mode = "off"
myst_enable_extensions = [
    "dollarmath",
    "attrs_inline",
    "html_image",
]
googleanalytics_id = "G-35GQBT0DZP"

bibtex_bibfiles = ["references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['_static']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "**/hidden",
    "user/index.rst",
    "user/manual/model/geomTransf/frame/index.rst",
    "user/manual/analysis/integrator/gimmeMCK.rst",
#   "user/manual/analysis/modalProperties.rst",
    "user/manual/analysis/responseSpectrumAnalysis.rst",
    "user/manual/model/damping/elementalDamping.rst",
    "user/manual/model/eleLoad.rst",
    "user/manual/model/elements/ASDEmbeddedNodeElement.rst",
    "user/manual/model/elements/FourNodeTetrahedron.rst",
    "user/manual/model/elements/frame/PointFrame.rst",
    "user/manual/model/elements/other/InertiaTruss.rst",
    "user/manual/model/elements/other/MEFI.rst",
    "user/manual/model/elements/other/ModElasticBeam.rst",
    "user/manual/model/elements/other/gradientInelasticBeamColumn.rst",
    "user/manual/model/elements/other/MVLEM_3D.rst",
    "user/manual/model/elements/other/SFI_MVLEM_3D.rst",
    "user/manual/model/elements/other/E_SFI.rst",
    "user/manual/model/elements/other/E_SFI_MVLEM_3D.rst",
    "user/manual/model/elements/grainfluid/7045-BbarBrickUP.rst",
    "user/manual/model/elements/grainfluid/7045-BbarBrickUP.md",
    "user/manual/model/elements/grainfluid/7046-BbarQuadUP.rst",
    "user/manual/model/elements/grainfluid/7066-BrickUP.rst",
    "user/manual/model/elements/grainfluid/7264-FourNodeQuadUP.rst",
    "user/manual/model/elements/grainfluid/7266-Four Node QuadUP.rst",
    "user/manual/model/elements/grainfluid/7419-NineFourNodeQuadUP.rst",
    "user/manual/model/elements/grainfluid/7612-SSPbrickUP.rst",
    "user/manual/model/elements/grainfluid/7614-SSPquadUP.rst",
    "user/manual/model/elements/grainfluid/7720-TwentyEightNodeBrickUP.rst",
    # "user/manual/model/elements/fluid/index.rst",
    "user/manual/materialCommands.rst",
    # "user/manual/material/ndMaterials/BoundingCamClay.rst",
    "user/manual/material/ndMaterials/PM4Sand.rst",
    "user/manual/material/ndMaterials/PM4Silt.rst",
    "user/manual/material/ndMaterials/PressureIndependentMultiYield.rst",
    "user/manual/material/ndMaterials/PressureIndependentMultiYieldExample1.rst",
    "user/manual/material/ndMaterials/PressureDependentMultiYield.rst",
    "user/manual/material/ndMaterials/PressureDependentMultiYield02.rst",
    "user/manual/material/ndMaterials/J2CyclicBoundingSurface.rst",
    "user/manual/material/ndMaterials/SAniSandMS.rst",
    "user/manual/material/ndMaterials/Orthotropic.rst",
    "user/manual/material/ndMaterials/Series3D.rst",
    "user/manual/material/ndMaterials/Parallel3D.rst",
    "user/manual/material/ndMaterials/InitStrain.rst",
    "user/manual/material/ndMaterials/ASDConcrete3D.rst",
    "user/manual/material/ndMaterials/ASDPlasticMaterial/*",
    "user/manual/material/ndMaterials/ASDPlasticMaterial.rst",
    "user/manual/material/ndMaterials/OrthotropicRAConcrete.rst",
    "user/manual/material/ndMaterials/SmearedSteelDoubleLayer.rst",
    "user/manual/section/ASDCoupledHinge3D.rst",
    "user/manual/section/LayeredMembraneSection.rst",
    "user/manual/section/ReinforcedConcreteLayeredMembraneSection.rst",
    "user/manual/output/getCrdTransfTags.rst",

    "user/manual/model/nodes/sp.rst",
    "user/manual/material/matTestCommands.rst",
    "user/manual/model/damping/elementalDamping/SecStifDamping.rst",
    "user/manual/model/damping/elementalDamping/URDDamping.rst",
    "user/manual/model/damping/elementalDamping/UniformDamping.rst",

    "user/manual/model/timeseries/MPAccTimeSeries.rst",
    "user/manual/model/timeseries/PeerNGAMotion.rst",
    "user/manual/model/timeseries/RampTimeSeries.rst",
    "user/manual/model/timeseries/peerMotion.rst",
    "user/manual/model/timeseries/pulseTimeSeries.rst",
    "user/manual/model/timeseries/rectangularTimeSeries.rst",
    "user/manual/model/timeseries/triangleTimeSeries.rst",
    "user/manual/model/timeseries/trigTimeSeries.rst",
]

# -- Options for HTML output -------------------------------------------------

html_baseurl       = "https://xara.so/"
sitemap_url_scheme = "{link}"

html_theme = "sphinx_book_theme" #"pydata_sphinx_theme" #"sphinx_rtd_theme"
html_show_sphinx = False
html_show_sourcelink = False

if html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        'navigation_depth': 6,
        'logo_only': True,
        'style_nav_header_background': 'white',
        'prev_next_buttons_location': None,
    }

else:
    html_theme_options = {
    #   'analytics_id': 'UA-2431545-1',
    #   "body_max_width": None,
        "show_prev_next": False,
        "logo": {
#         "image_light": html_logo,
#         "image_dark": "_static/logo-dark.png",
          "link": html_baseurl, # "index.html",
          "text": f'<span class="lead display-3">{project}</span>',
#         "alt_text": "xara docs - Home",
        }
    }

if "book" in html_theme:
    html_theme_options.update({
        "use_download_button":  False,
        "use_edit_page_button": False,
        "article_header_start": ["toggle-primary-sidebar.html", "breadcrumbs"]
    })

g = "https://gallery.stairlab.io"
html_favicon = '_static/images/favicon.ico'
html_context = {
    "root_doc": root_doc,
    "description": description,
    "github_user": "peer-open-source",
    "github_repo": "xara",
#   "doc_path": "<path-from-root-to-your-docs>",

    # HOME
    "examples": [
            # {"title": "Basics",      "link": f"{g}/examples/plane-0002/",     "image": "../_static/images/gallery/Example6.png", "description": "Learn the basics of drawing models."},
            # {"title": "Detailing",   "link": f"{g}/examples/example7/",     "image": "../_static/images/gallery/ShellFrame.png", "description": "."},
            # {"title": "Finite Rotations",  "link": f"{g}/examples/framecircle/",  "image": "../_static/images/gallery/ShellCircle-576x324.webp", "description": "Render finite deformations in constrained members like Cosserat rods and shells."},

            # {"title": "Frames",      "link": f"{g}/examples/portal-moments/",     "image": "../_static/images/gallery/moments.png", "description": "Render structural models with extruded sections."},
#           {"title": "Sections",    "link": f"{g}/examples/framesections/",     "image": "../_static/images/gallery/Torsion.png", "description": "Detailed analysis of structural cross sections."},
            # {"title": "Versatility",     "link": f"{g}/examples/cablestayed/",  "image": "../_static/images/gallery/CableStayed02-576x324.webp", "description": "Import models from commercial platforms like ABAQUS."},
#           {"title": "Motions",     "link": f"{g}/examples/framehelix/",  "image": "../_static/images/gallery/sign-light-2800x2558.webp", "description": "Coming soon."},
#           {"title": "Interoperability", "link": f"{g}/examples/cablestayed/",  "image": "../_static/images/gallery/CableStayed02-576x324.webp", "description": "Coming soon."},
    ],
    "features": [
        # {"title": "Fast", "body": "Core components have been refactored to leverage modern C++ features, which has furnished substantial performance improvements over the alternative serial OpenSees interpreters."},
        # {"title": "Free", "body": "All source code contributed to xara is licensed under a <em>pure</em> BSD."},
        # {"title": "Robust", "body": '<em>xara</em> is designed from the ground up for use in production environments like <a href="https://structures.live">structures.live</a>'},
    ],
    "home_image": "_static/images/CableStayed02.png"
}

#  'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B,

html_css_files = [
    'css/custom.css'
] + [
    'css/home-css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/home-css/").glob("vars*.css")
] + [
     'css/css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/css/").glob("*.css")
] + [
    "css/veux.css",
]

html_secnum_suffix = " "

mathjax3_config = {
  "loader": {"load": ['[tex]/color']},
  "tex": {
      "packages": {'[+]': ['color']},
      "inlineMath": [['$', '$'], ['\\(', '\\)']]
  }
}



from pathlib import Path
if XARA_GALLERY:
    from xara_sphinx_gallery import GalleryConfig, generate_gallery
    # generate_gallery(
    #     GalleryConfig(
    #     examples_dirs="../examples",
    #     gallery_dirs="gallery",
    #     target_prefix="",
    #     root_dir=Path(__file__).parent,
    #     notebook_thumbnail_strategy="markdown",
    #     thumbnail_strategy="first",
    #     exclude_assets=[
    #         # "meta.yml",
    #         "*.tcl",
    #         "GALLERY_HEADER.rst"
    #     ]
    #     # base_gallery=True,
    #     )
    # )
else:
    from myst_sphinx_gallery import GalleryConfig, generate_gallery

    from myst_sphinx_gallery.gallery import ExampleConverter

    def _thumb_file_rel(self, thumb_file):
        root = Path(self.config.root_dir).resolve()
        return "/" + Path(thumb_file).resolve().relative_to(root).as_posix()

    ExampleConverter.thumb_file_rel = _thumb_file_rel


from gallery import Galleries, OutputDocs, OutputRoot, build

# build(OutputRoot)  # regenerate the source tree


Here = Path(__file__).parent
_example_dirs = [
    str((OutputRoot/g["directory"]).resolve().relative_to(Here,walk_up=True)) for g in Galleries
]
_gallery_dirs = [
    f"{(OutputDocs/g['directory']).resolve().relative_to(Here)}" for g in Galleries
]
# _gallery_dirs = [
#     f'_g_{g["directory"]}' for g in Galleries
# ] 

generate_gallery(
    GalleryConfig(
        examples_dirs=_example_dirs,
        gallery_dirs=_gallery_dirs,
        root_dir=Path(__file__).resolve().parent,
        notebook_thumbnail_strategy="markdown",#"code",#
        thumbnail_strategy="first",
        target_prefix="",
        remove_thumbnail_after_build=False,
        base_gallery=True,
    )
)
