import array

#function for seperating the tasks
def print_section_header(title):
    print("="*10)
    print(f"SECTION: {title}")
    print("="*10)

def values():
    # 4 create buildings
    attendance_data = [85, 92, 78, 90]
    buildings = ["Building A", "Building B", "Building C", "Building D"]

    # calcularions
    total = sum(attendance_data)
    average = total / len(attendance_data)
    minimum = min(attendance_data)
    maximum = max(attendance_data)

    return attendance_data, buildings, total, average, minimum, maximum


def section_1_integers(attendance_data, buildings, total, average, minimum, maximum):
    print_section_header("INTEGERS")
    print(f"  Total participants: {total}")
    print(f"  Average attendance: {average:.1f}")
    print(f"  Minimum attendance: {minimum}")
    print(f"  Maximum attendance: {maximum}")
    return attendance_data, buildings, total, average, minimum, maximum


def section_2_strings(attendance_data, buildings, average):
    print_section_header("STRINGS")

    # detail report
    print("\nDetailed building report:")
    for i, (building, count) in enumerate(zip(buildings, attendance_data)):
        status = "above Average" if count > average else "Below Average"
        detail_line = f"{building}: {count} participants ({status})"
        print(f"  {detail_line}")

def section_3_booleans(average, minimum, attendance_data, buildings):
    print_section_header("BOOLEANS")

    #set thresholds
    threshold_standard = 85
    threshold_minimum = 75

    print(f"Thresholds: expected standard > {threshold_standard}, minimum > {threshold_minimum}")

    #save boolean in variable
    above_avg_threshold = average > threshold_standard
    above_min_threshold = minimum > threshold_minimum

    print(f"\nSimple Checks:")
    print(f"  Average above threshold: {above_avg_threshold}")
    print(f"  Minimum above threshold: {above_min_threshold}")

    #check each building
    for building, count in zip(buildings, attendance_data):
        if count > threshold_standard:
            print (f"{building}: Above standard")
        else:
            print (f"{building}: Below standard")



def section_4_lists(attendance_data, buildings):
    print_section_header("LISTS - List Operations")

    # create a copy to work with
    work_list = attendance_data.copy()
    work_buildings = buildings.copy()

    # add element
    new_attendance = 88
    new_building = "Building E"
    work_list.append(new_attendance)
    work_buildings.append(new_building)

    print(f"After adding {new_building} ({new_attendance} participants):")
    for building, count in zip(work_buildings, work_list):
        print(f"  {building}: {count}")

    # remove lowest attendence
    min_index = work_list.index(min(work_list))
    remove_count = work_list.pop(min_index)
    remove_building = work_buildings.pop(min_index)

    print(f"\nAfter removing {remove_building} (lowest: {remove_count}):")
    for building, count in zip(work_buildings, work_list):
        print(f"  {building}: {count}")

    #sort list by atendence
    combined = list(zip(work_list, work_buildings))
    combined.sort(reverse=True) #high first
    work_list_sorted = [count for count, building in combined]
    work_buildings_sorted = [building for count, building in combined]

    print(f"\nAfter sorting (highest to lowest):")
    for building, count in zip(work_buildings_sorted, work_list_sorted):
        print(f"  {building}: {count}")

    return work_list_sorted


def section_5_arrays(attendance_data):
    print_section_header("ARRAYS")

    # set py array
    subset_data = attendance_data[:3]
    attendance_array = array.array('i', subset_data)  # 'i' for integers

    # compare
    list_sum = sum(subset_data)
    array_sum = sum(attendance_array)

    print("List vs Array comparison:")
    print(f"  Original list (first 3): {subset_data}")
    print(f"  Python array: {attendance_array}")
    print(f"  List sum: {list_sum}")
    print(f"  Array sum: {array_sum}")


def section_6_dictionaries(attendance_data, buildings):
    print_section_header("DICTIONARIES")

    #create a list of dictionauies
    records = []
    for i, (building, count) in enumerate(zip(buildings, attendance_data), 1):
        record = {
            'id': i,
            'name': building,
            'value': count
        }
        records.append(record)

    print("Original Records:")
    for record in records:
        print(f"  ID {record['id']}: {record['name']} = {record['value']} participants")

    #update
    for record in records:
        if record['id'] == 2:
            old_value = record['value']
            record['value'] = 95  # Update auf 95
            print(f"\nUpdated ID 2: {record['name']} from {old_value} to {record['value']}")
            break

    #delete
    for i, record in enumerate(records):
      if record['id'] == 3:
        deleted_record = records.pop(i)  # Entfernen
        print(f"\nDeleted ID 3: {record['name']}")
        break

    print(f"\nAfter modifications:")
    for record in records:
        print(f"  ID {record['id']}: {record['name']} = {record['value']} participants")

    # calculations
    total_value = sum(record['value'] for record in records)
    record_count = len(records)
    average_value = total_value / record_count if record_count > 0 else 0

    print(f"\nFinal Statistics:")
    print(f"  Total participants: {total_value}")
    print(f"  Number of records: {record_count}")
    print(f"  Average per record: {average_value:.1f}")

#for all results
def main():
    attendance_data, buildings, total, average, minimum, maximum = values()
    section_1_integers(attendance_data, buildings, total, average, minimum, maximum)
    section_2_strings(attendance_data, buildings, average)
    section_3_booleans(average, minimum, attendance_data, buildings)
    sorted_list = section_4_lists(attendance_data, buildings)
    section_5_arrays(attendance_data)
    section_6_dictionaries(attendance_data, buildings)

if __name__ == "__main__":
    main()
