import subprocess

# Step 1: Run cme_data.py
print("Running cme_data.py...")
subprocess.run(["python3", "scripts/cme_data.py"], check=True)

# Step 2: Run gst_data.py
print("Running gst_data.py...")
subprocess.run(["python3", "scripts/gst_data.py"], check=True)

# Step 3: Run merge_data.py
print("Running merge_data.py...")
subprocess.run(["python3", "scripts/merge_data.py"], check=True)

print("All scripts have been executed successfully!")
