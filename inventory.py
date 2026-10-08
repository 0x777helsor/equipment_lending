from data import resources

def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None        

def add_resource(resource_id, name, category, total):
    if find_resource(resource_id) is not None:
        return False, "Resoure ID already exists."
    if total <= 0:
        return False, "Total units must be greater than 0."

    new_resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total,
    }


    resources.append(new_resource)

    return True, "Resource added successfully"

def list_resources():
    return resources

def search_resources(name):
    results = []

    for resource in resources:
        if name.lower() in resource["name"].lower():
            results.append(resource)

    return results

def filter_by_category(category):
    results = []

    for resource in resources:
        if resource["category"].lower() == category.lower():
            results.append(resource)

    return results