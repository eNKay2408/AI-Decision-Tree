import os
import subprocess
import sys
import traceback

def run():
    # Current directory
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Working in directory: {workspace_dir}")
    
    # Install requirements
    print("Installing requirements...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False
        
    # Execute notebook
    notebook_path = os.path.join(workspace_dir, "notebooks", "02_palmer_penguins_analysis.ipynb")
    output_path = os.path.join(workspace_dir, "notebooks", "02_palmer_penguins_analysis_executed.ipynb")
    
    print(f"Executing notebook: {notebook_path}")
    print(f"Output will be saved to: {output_path}")
    
    # Kiểm tra tồn tại của file
    if not os.path.exists(notebook_path):
        print(f"ERROR: Notebook file not found: {notebook_path}")
        return False
    
    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "jupyter", "nbconvert", 
                "--to", "notebook", 
                "--execute", 
                "--ExecutePreprocessor.timeout=600",
                "--output", os.path.basename(output_path),
                "--output-dir", os.path.dirname(output_path),
                notebook_path
            ],
            check=False,  # Don't raise an exception on non-zero exit
            capture_output=True,
            text=True
        )
        
        print(f"Process exit code: {result.returncode}")
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
            
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
            
        if result.returncode == 0:
            print("Notebook execution completed successfully!")
            return True
        else:
            print("Notebook execution failed!")
            return False
            
    except Exception as e:
        print(f"Error executing notebook: {e}")
        traceback.print_exc()
        return False
        
if __name__ == "__main__":
    success = run()
    sys.exit(0 if success else 1)
