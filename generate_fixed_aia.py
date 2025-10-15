#!/usr/bin/env python3
"""
generate_fixed_aia.py
Generate a corrected .aia (ZIP) with minimal structure Kodular/MIT App Inventor expects.
Output: IoT_Monitoring_Wokwi_Kodular_fixed.aia
Run: python generate_fixed_aia.py
"""
import zipfile, datetime, textwrap, os, sys

PROJECT_NAME = "IoT_Monitoring_Wokwi_Kodular_fixed"
OUT_FILE = PROJECT_NAME + ".aia"
TS = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# project.properties (must exist)
project_properties = textwrap.dedent(f"""\
name={PROJECT_NAME}
version=1
lastSaved={TS}
""")

# Very small but correctly named youngandroidproject (lowercase) file
youngandroidproject = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<youngandroidproject>
  <projectname>{project}</projectname>
  <createDate>{date}</createDate>
</youngandroidproject>
""").format(project=PROJECT_NAME, date=TS)

# Minimal SCM for screens — slightly richer structure but still simple.
# Kodular expects well-formed scm content; this is a reasonable minimal placeholder.
def make_scm(screen_name, title):
    return textwrap.dedent(f"""\
    <?xml version="1.0" encoding="UTF-8"?>
    <scm>
      <Screen1 name="{screen_name}" title="{title}">
        <Designer>
          <Properties>
            <Property name="AppName" value="{PROJECT_NAME}"/>
            <Property name="Title" value="{title}"/>
          </Properties>
        </Designer>
        <Components>
          <!-- Minimal placeholder components (create UI in Designer after import) -->
          <Component type="com.google.appinventor.components.runtime.Label" id="lbl_{screen_name}_placeholder">
            <Property name="Text" value="Placeholder: {title}"/>
          </Component>
        </Components>
        <Blocks/>
      </Screen1>
    </scm>
    """)

# README for the archive (helpful)
readme = textwrap.dedent(f"""\
IoT Monitoring Wokwi - Kodular (.aia fixed)
Generated: {TS}

This .aia is a minimal, corrected-structure placeholder to allow Kodular importer to accept it.
After importing, please:
- Add the MQTT extension (Paho/Arduino or your preferred)
- Recreate the UI cards and blocks per the repo's components/ and blocks/ files (they are included as text files)
""")

# Include human-readable component & block instruction files (so you can rebuild quickly)
components_txt = {
    "components/LoginScreen.txt": "See your GitHub repo components/LoginScreen.txt\n(Use it to build LoginScreen in Designer)",
    "components/AdminDashboard.txt": "See your GitHub repo components/AdminDashboard.txt",
    "components/HistoryScreen.txt": "See your GitHub repo components/HistoryScreen.txt",
    "components/Sidebar.txt": "See your GitHub repo components/Sidebar.txt",
}
blocks_txt = {
    "blocks/LoginScreen_blocks.txt": "See your GitHub repo blocks/LoginScreen_blocks.txt",
    "blocks/AdminDashboard_blocks.txt": "See your GitHub repo blocks/AdminDashboard_blocks.txt",
    "blocks/HistoryScreen_blocks.txt": "See your GitHub repo blocks/HistoryScreen_blocks.txt",
    "blocks/Helpers.txt": "See your GitHub repo blocks/Helpers.txt",
}

# Screens we will include as assets/*.scm
screens = ["LoginScreen", "AdminDashboard", "HistoryScreen", "Sidebar"]

def build_aia(out_path):
    # Remove existing output
    if os.path.exists(out_path):
        os.remove(out_path)
    with zipfile.ZipFile(out_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        # Required core files
        z.writestr("project.properties", project_properties)
        # IMPORTANT: this filename must be exactly 'youngandroidproject' (lowercase, no extension)
        z.writestr("youngandroidproject", youngandroidproject)
        # Assets: scm files for each screen
        for s in screens:
            scm_name = f"assets/{s}.scm"
            z.writestr(scm_name, make_scm(s, s))
        # Add README and helper text files to help rebuild blocks/UI quickly
        z.writestr("README.txt", readme)
        for k, v in components_txt.items():
            z.writestr(k, v)
        for k, v in blocks_txt.items():
            z.writestr(k, v)

    print("Created:", out_path)
    print("Import this .aia via Kodular: Projects -> Import project (.aia) from my computer")
    print("If Kodular still rejects it, copy the exact error message here and I'll adapt the .scm contents accordingly.")

if __name__ == "__main__":
    build_aia(OUT_FILE)
