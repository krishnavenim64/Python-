Import os



Directory = “C:/Users/Revanth/Documents”

For index, filename in enumerate(os.listdir(directory)):

    Old_path = os.path.join(directory, filename)

    New_path = os.path.join(directory, f”file_{index}.txt”)

    Os.rename(old_path, new_path)



Print(“Files renamed successfully!”)

