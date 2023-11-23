import os
import tempfile
import sublime, sublime_plugin
import subprocess


class HtmlToSlimFromFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    source = self.view.file_name()
    if source.endswith(".erb"):
      target = source.replace('.erb', '.slim')
    if source.endswith(".html"):
      target = source + '.slim'
    if target:
      Slim.convert(source, target)
      self.view.window().open_file(target)

  def is_enabled(self):
    return True #return (self.view.file_name().endswith(".html") or self.view.file_name().endswith(".erb"))

class HtmlToSlimFromSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        html = self.view.substr(region)
        slim = Slim.buffer(html)
        if slim != None:
          self.view.replace(edit, region, slim)

  def is_enabled(self):
    return True #return self.view.file_name().endswith(".slim")

class HtmlToSlimFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    html = sublime.get_clipboard()
    slim = Slim.buffer(html)
    if slim != None:
      for region in self.view.sel():
        self.view.replace(edit, region, slim)

  def is_enabled(self):
    return True #return self.view.file_name().endswith(".slim")


class Slim:
    @classmethod
    def convert(cls, html_file, slim_file):
        settings = sublime.load_settings("HTML2Slim.sublime-settings")
        default_rails_path = settings.get("default_rails_path")
        default_user_path = settings.get("default_user_path")
        # print("default_rails_path: ", default_rails_path)

        # Append to the existing PATH
        os.environ['PATH'] = "{}/.cargo/bin:/usr/local/sbin:/usr/local/bin:{}/opt/anaconda3/bin:{}/opt/anaconda3/condabin:{}/.pyenv/shims:{}/.pyenv/bin:{}/.rbenv/shims:{}/.rbenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:{}/.cargo/bin".format(default_user_path, default_user_path, default_user_path, default_user_path, default_user_path, default_user_path, default_user_path, default_user_path)

        rbenv_dir = "RBENV_DIR=" + default_rails_path
        # print("Modified PATH:", os.environ['PATH'])

        cmd = "{} rbenv exec erb2slim {} {}".format(rbenv_dir, html_file, slim_file)
        # print("Executing command:", cmd)

        try:
            process = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, errors = process.communicate()
            if process.returncode != 0:
              print("Command failed with exit code:", process.returncode)
              print("Output:", output.decode())
              print("Errors:", errors.decode())
              return False
        except Exception as e:
            print("Error during command execution:", e)
            return False
        return True
    
    @classmethod
    def buffer(cls, html):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as html_temp:
            html_file = html_temp.name
            html_temp.write(html.encode())
            # print("HTML file written:", html_file)  # Debug: Confirm file write

        slim_file = html_file + '.slim'
        
        if not cls.convert(html_file, slim_file):
            print("Conversion failed. Slim file not created.")
            return None

        if not os.path.exists(slim_file):
            print("Slim file does not exist:", slim_file)
            return None

        with open(slim_file, 'r') as file:
            slim_content = file.read()
        
        os.remove(html_file)
        os.remove(slim_file)
        
        return slim_content