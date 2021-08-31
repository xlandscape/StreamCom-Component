"""
Script for documenting the code of the StreamCom component.
"""
import os
import base.documentation
import StreamCom

root_folder = os.path.abspath(os.path.join(os.path.dirname(base.__file__), ".."))
base.documentation.document_component(
    StreamCom.StreamCom("StreamCom", None, None),
    os.path.join(root_folder, "..", "variant", "StreamCom", "README.md"),
    os.path.join(root_folder, "..", "variant", "mc.xml"),
    "StreamCom1_StepsRiverNetwork"
)
base.documentation.write_changelog(
    "StreamCom component",
    StreamCom.StreamCom.VERSION,
    os.path.join(root_folder, "..", "variant", "StreamCom", "CHANGELOG.md")
)
base.documentation.write_contribution_notes(
    os.path.join(root_folder, "..", "variant", "StreamCom", "CONTRIBUTING.md"))
