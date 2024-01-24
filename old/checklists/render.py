
import yaml
import os
from optparse import OptionParser
from jinja2 import (
    Environment, FileSystemLoader, StrictUndefined,
)
parser = OptionParser()
parser.add_option( "-t", "--template", dest="template", metavar="FILE", action="store",)
parser.add_option( "-d", "--data", dest="data", metavar="FILE", action="store",)

opts, args = parser.parse_args()

basedir = os.path.dirname(opts.template)
templatename = os.path.basename(opts.template)
outfile = os.path.join(basedir, templatename.replace(".jinja", ".html"))
datafile = os.path.join(basedir, opts.data)

with open(datafile, 'r') as f:
    data = yaml.safe_load(f) or {}

env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__)),
    keep_trailing_newline=True,
    undefined=StrictUndefined
)

relative_from = os.path.normpath(os.path.dirname(__file__))
template_load_path = os.path.relpath(opts.template, start=relative_from)

with open(outfile, "w") as f:
    f.write(env.get_template(template_load_path).render(data))

