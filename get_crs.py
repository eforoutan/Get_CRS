import geopandas as gpd
import csv
import sys

def get_crs_info(input_shapefile):
    try:
        gdf = gpd.read_file(input_shapefile)
    except Exception as e:
        print(f"Error reading input shapefile: {e}")
        return None, None, None, None

    # Extract CRS information
    crs = gdf.crs

    if crs is None:
        return None, None, None, None  # No CRS found

    # Determine if CRS is projected and get unit
    is_projected = crs.is_projected
    unit = crs.axis_info[0].unit_name if is_projected else "degrees"

    # Extract EPSG code (if available)
    epsg_code = crs.to_epsg() if crs.to_epsg() is not None else "Unknown"

    return crs, is_projected, unit, epsg_code


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_crs.py <input_shapefile>")
        sys.exit(1)

    input_shapefile = sys.argv[1]
    crs, is_projected, unit, epsg_code = get_crs_info(input_shapefile)

    if crs:
        crs_str = str(crs)
        proj_status = "Projected" if is_projected else "Geographic"
        
        # Print results to console
        print(f"CRS: {crs_str}")
        print(f"Type: {proj_status}")
        print(f"Unit: {unit}")
        print(f"EPSG: {epsg_code}")

        # Write results to CSV
        output_csv = "crs_info.csv"
        try:
            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["CRS", "Type", "Unit", "EPSG"])
                writer.writeheader()
                writer.writerow({"CRS": crs_str, "Type": proj_status, "Unit": unit, "EPSG": epsg_code})
            print(f"CRS information successfully written to '{output_csv}'.")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")
    else:
        print("Failed to process the shapefile.")
