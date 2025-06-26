#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>
#include <algorithm>

namespace py = pybind11;

// Example function: Accelerated sum of amounts
double sum_amounts(const std::vector<double>& amounts) {
    double total = 0.0;
    for (double amt : amounts) {
        total += amt;
    }
    return total;
}

// Example function: Filter descriptions containing a keyword (case-insensitive)
std::vector<std::string> filter_descriptions(const std::vector<std::string>& descriptions, const std::string& keyword) {
    std::vector<std::string> result;
    std::string lower_keyword = keyword;
    std::transform(lower_keyword.begin(), lower_keyword.end(), lower_keyword.begin(), ::tolower);

    for (const auto& desc : descriptions) {
        std::string lower_desc = desc;
        std::transform(lower_desc.begin(), lower_desc.end(), lower_desc.begin(), ::tolower);
        if (lower_desc.find(lower_keyword) != std::string::npos) {
            result.push_back(desc);
        }
    }
    return result;
}

PYBIND11_MODULE(native_extension, m) {
    m.doc() = "Native extension module for performance-critical functions";

    m.def("sum_amounts", &sum_amounts, "Sum a list of amounts");
    m.def("filter_descriptions", &filter_descriptions, "Filter descriptions by keyword");
}
